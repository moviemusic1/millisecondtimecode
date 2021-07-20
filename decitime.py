#!/usr/bin/env python3
'''
Copyright (C) 2021  lymnyx

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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
    if '.' in args[2]:
        timestamp = int(''.join(args[2].split('.')))
    else:
        timestamp = int(args[2])
    time = datetime.utcfromtimestamp(timestamp / 10).strftime('%m %d %Y (%H:%M:%S)').split(' ')
    time[0] = months[int(time[0])-1]
    time[1] = time[1] + rth(int(time[1]))
    time = ' '.join(time)
    print('This timestamp is from ' + time + '.')

if len(sys.argv) > 1:
    if sys.argv[1].lower() == 'get': get()
    else: give(sys.argv)
else:
    get()
