##
# Created on 14, October, 2014
# test the efficiency of multiprocess
# @author: chenzhi

from multiprocessing import Process, Queue
import os, time, random

def mysum(begin, end, q):
    i = begin
    sums = 0
    while(i < end):
        sums += i
        i += 1
    q.put(sums)
    
if __name__ == '__main__':
    maximum = 10000000
    start = time.time()
    sums = 0
    i = 0
    while(i < maximum):
        sums += i
        i += 1
    end = time.time()
    print str(end - start), 's'
    print sums
    
    q = Queue()
    start = time.time()
    p1 = Process(target=mysum, args=(0, maximum / 2, q, ))
    p2 = Process(target=mysum, args=(maximum / 2 + 1, maximum, q, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print str(end - start), 's'
    print str(q.get() + q.get())
    