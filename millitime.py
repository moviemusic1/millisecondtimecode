import sys, time
from datetime import datetime

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rths = ['st', 'nd', 'rd', 'th']

def rth(num):
    if num in (1, 21, 31): return rths[0]
    elif num in (2, 22): return rths[1]
    elif num in (3, 23): return rths[2]
    else: return rths[3]

def get():
    print('Currently: ' + str(int(time.time() * 10) / 10))

def give(args):
    if '.' in args[1]:
        timestamp = int(args[1].split('.')[0])
    else:
        timestamp = int(args[1])
    time = datetime.utcfromtimestamp(timestamp).strftime('%m %d %Y (%H:%M:%S)').split(' ')
    time[0] = months[int(time[0])-1]
    time[1] = time[1] + rth(int(time[1]))
    time = ' '.join(time)
    print('This timestamp is from ' + time + '.')

if len(sys.argv) > 1:
    if sys.argv[1].lower() == 'get': get()
    else: give(sys.argv)
else:
    get()
