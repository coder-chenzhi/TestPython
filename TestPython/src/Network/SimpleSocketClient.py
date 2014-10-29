'''
Created on Oct 28, 2014

@author: Chenzhi
'''
import socket, os, sys
from multiprocessing import Process, Queue, Pipe

ip = '127.0.0.1'    # which ip to connected
port = 10086  # which port to connected
maxRecv = 1024  # max length to receive

def listenStdin(msg, fn, pipe):
    '''
    start a process to listen to stdin, and whenever receive any
    input from stdin, transprot it to Queue msg.
    
    Args:
        msg: a Queue to share message between processes.
        fn: redirect system stdin, in order to use stdin in child process.
        pipe: communicate between processes
        
    '''
    
    inputs = ''  # store input from stdin
    sys.stdin  = os.fdopen(fn)
    
    '''wait for connection established.'''
    while True:
        if pipe.recv() == True:
            print "You can chat with server now! Type 'exit' to finish this conversation.:)"
            break
    
    while True:
        inputs = raw_input('')
        msg.put(inputs)
        if inputs == 'exit':
            print 'Thanks for using!'
            break
            
def sendMessage(ip, host, msg, pipe):
    '''
    start a process to new a socket connected to ip:port, and 
    transport any message from Queue msg to ip:port
    
    Args:
        ip: server ip to connected
        port: serve port to connected
        msg: a Queue share message between processes
        pipe: communicate between processes
        
    '''
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print "Try to connected server %s:%d..." % (ip, host)
        sock.connect((ip, port))
    except Exception, e:
        print 'Error occurred when try to connected server %s:%d' % (ip, host)
        print e
        sock.close()
        return 
    print 'Connection established.'
    pipe.send(True) # send message to listenProc process
    
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
    pipe_a, pipe_b = Pipe()
    fn = sys.stdin.fileno()
    listenProc = Process(target=listenStdin, args=(msg, fn, pipe_a, ))
    sendProc = Process(target=sendMessage, args=(ip, port, msg, pipe_b, ))
    listenProc.start()
    sendProc.start()    