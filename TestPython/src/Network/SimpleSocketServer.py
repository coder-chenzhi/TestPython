'''
Created on Oct 28, 2014

@author: Chenzhi
'''

import socket

ip = '127.0.0.1'
port = 10086
maxRecv = 65536 
if __name__ == '__main__':
    msg = ''
    sock = None
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
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
            sock.sendall('Got message!\n')
    s.close() 
    