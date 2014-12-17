'''
@author: zhichen
@date: 16, Dec, 2014

'''

import time
import logging

LOG_PATH = '/home/ubuntu/Documents/log/'

def get_current_time():
    localtime   = time.localtime()
    timeString  = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    return timeString


logging.basicConfig(filename=LOG_PATH + get_current_time() + '.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')