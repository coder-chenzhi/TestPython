'''
Created on Oct 30, 2014

@author: Chenzhi
'''

from multiprocessing import Pipe
from multiprocessing.dummy import Process

def sendProc(pipe):
    pipe.send(True)
    
def recvProc(pipe):
    while True:
        var = pipe.recv()
        if var:
            break
    print 'I am free!'
    
if __name__ == '__main__':
    parent_pipe, child_pipe = Pipe()
    send_proc = Process(target=sendProc, args=(parent_pipe,))
    recv_proc = Process(target=recvProc, args=(child_pipe,))
    send_proc.start()
    recv_proc.start()