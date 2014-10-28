##
# Created on Oct 12, 2014
# Test List comprehensions
# @author: Chenzhi

if __name__ == '__main__':
    L = ['HELLO', 'WORLD', 11]
    print [s.lower() for s in L if isinstance(s, str) ]