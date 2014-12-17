'''
Created On 24, Nov, 2014
@author: ZhiChen

'''

import time

if __name__ == '__main__':
    # first test
    print 'first test'
    s1 = time.strptime('18:50:59', '%H:%M:%S')
    s2 = time.strptime('18:05:59', '%H:%M:%S')
    s3 = time.strptime('09:05:01', '%H:%M:%S')
    print sorted([s1, s2, s3])
    print '-----------------------------------------'
    # second test
    print 'second test'
    localtime   = time.localtime()
    timeString  = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    print timeString