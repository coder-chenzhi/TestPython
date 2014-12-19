'''
@author: zhichen
@date: 19, Dec, 2014

test accuracy of sleep()
The result shows that sleep isn't accuracy, sometimes longer than the time you set,
which is caused by time slice switch.
'''

import time

loop = 200
sleep_time = 0.025

start_time = time.time() * 1000
for i in range(loop):
    time.sleep(sleep_time)

print time.time() * 1000 - start_time
