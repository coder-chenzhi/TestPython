'''

'''

import json

code = json.dumps([{'metric_name': 'memory_metric'}, {'used': 1024}, {'total': 2048}])
decode = json.loads(code)

print decode, type(decode)