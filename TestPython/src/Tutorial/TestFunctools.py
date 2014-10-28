'''
Created on 14, October, 2014
 
@author: chenzhi
'''

import functools

if __name__ == '__main__':
    reverseSort = functools.partial(sorted, reverse = True)
    print reverseSort([5,9,2,4,7])