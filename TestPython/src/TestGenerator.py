##
# Created on Oct 12, 2014
# Test Generator
# @author: Chenzhi

import logging

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

if __name__ == '__main__':
    # generator doesn't have hasNext() method,
    # it will throw StopIteration exception
    # when there isn't next element 
    lst = (i for i in range(0,2))
    print 'test throwing StopIteration...'
    try:
        print lst.next()
        print lst.next()
        print lst.next()
        print lst.next()
    except Exception as e:
        logging.exception(e) # this will allow code continue execute after catch an exception
        print 'catch it!'
        
    # iterate the generator
    print 'iterate a generator...'
    lst = (i for i in range(0,2))
    for e in lst:
        print e
        
    # test yield
    print 'test yield...'
    for n in fib(6):
        print n