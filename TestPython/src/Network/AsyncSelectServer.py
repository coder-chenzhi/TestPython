'''
Created on Oct 28, 2014
Use select module to support asynchronous

@author: Chenzhi
'''

import socket
import sys
import os
import select
from multiprocessing import Process, Pipe

def cmd(pipe, stdin):
    '''
    server command console, can receive command from stdin
    
    Args:
        pipe: pipe to communicate with other servers
        stdin: redirect main process stdin
    
    '''
    
    sys.stdin  = os.fdopen(stdin)
    while True:
        inputs = raw_input('')
        pipe.send(inputs)


def conn():
    '''
    manage connection
    
    '''

    ip = '127.0.0.1'
    port = 10086
    maxRecv = 65536 
    msg = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(5)
    inputs = [s]
    while True:
        readable, _, _ = select.select(inputs, [], [])
        for r in readable:
            if r is s:
                cn, addr = s.accept()
                print 'Accept new connection from %s:%s...' % addr
                inputs.append(cn)
            else:
                msg = r.recv(maxRecv)
                print 'receive message :{', msg, '} from %s:%s' % r.getpeername()
                if msg == 'exit':
                    inputs.remove(r)
                    r.close()                    
                else:
                    r.sendall( 'Server got message!')
    s.close() 
    
if __name__ == '__main__':
    mainPipe, cmdPipe = Pipe()
    stdin = sys.stdin.fileno()
    connProc = Process(target=conn, args=())
    cmdProc = Process(target=cmd, args=(cmdPipe, stdin, ))
    connProc.start()
    cmdProc.start()
    while True:
        command = mainPipe.recv()
        if command == 'exit':
            connProc.terminate()
            cmdProc.terminate()
            print 'Server terminated!'
            break
        