'''
Created On 24, Nov, 2014
@author: ZhiChen

'''

import time

if __name__ == '__main__':
    s1 = time.strptime('18:50:59', '%H:%M:%S')
    s2 = time.strptime('18:05:59', '%H:%M:%S')
    s3 = time.strptime('09:05:01', '%H:%M:%S')
    print sorted([s1, s2, s3])
