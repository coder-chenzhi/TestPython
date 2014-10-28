import re

s = 'stat_client1'
m = re.search('\d+', 'stat_client1234')
print m.group(0)