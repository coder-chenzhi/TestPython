'''
Created on Oct 28, 2014

@author: Chenzhi
'''
import socket, os, sys
from multiprocessing import Process, Queue

ip = '127.0.0.1'    # which ip to connect
port = 10086  # which port to connect
maxRecv = 65536

def listenStdin(msg, fn):
    '''
    start a process to listen to stdin, and whenever receive any
    input from stdin, transprot it to Queue msg.
    
    Args:
        msg: a Queue to share message between processes.
        fn: redirect system stdin, to use stdin in child process
        
    '''
    
    first = True    # flag to indicate if this is the first time
    inputs = ''  # store input from stdin
    sys.stdin  = os.fdopen(fn)
    
    while True:
        if first == True:
            first = False
            inputs = raw_input("Welcome! You can chat with server now!")
        else:
            inputs = raw_input('')
        
        msg.put(inputs)
        if inputs == 'exit':
            print 'Thanks for using!'
            break
            
def sendMessage(ip, host, msg):
    '''
    start a process to new a socket connect to ip:port, and 
    transport any message from Queue msg to ip:port
    
    Args:
        ip: server ip to connect
        port: serve port to connect
        msg: a Queue share message between processes
    
    '''
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    
    while True:
        inputs = msg.get()
        sock.sendall(inputs)
        if inputs == 'exit':
            break
        else: 
            print sock.recv(maxRecv)
    sock.close()
    
if __name__ == '__main__':
    msg = Queue()
    fn = sys.stdin.fileno()
    listenProc = Process(target=listenStdin, args=(msg, fn))
    sendProc = Process(target=sendMessage, args=(ip, port, msg, ))
    listenProc.start()
    sendProc.start()    