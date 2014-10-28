'''
Created on Oct 29, 2014

@author: Chenzhi
'''
from multiprocessing import Queue

q = Queue()
q.put(1)
print q.get()
print q.get()