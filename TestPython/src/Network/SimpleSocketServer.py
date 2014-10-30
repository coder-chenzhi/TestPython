'''
Created on Oct 28, 2014

@author: Chenzhi
'''

import socket
import sys
import os
from multiprocessing import Process, Pipe

def cmd(pipe, stdin):
    '''
    server command console
    
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
    sock = None
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(5)
    while True:
        print 'Waiting for connection...'
        sock, addr = s.accept()
        print 'Accept new connection from %s:%s...' % addr
        while True:
            msg = sock.recv(maxRecv)
            print 'receive message :{', msg, '} from %s:%s' % addr
            if msg == 'exit':
                sock.close()
                break
            else:
                sock.sendall( 'Server got message!')
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
        