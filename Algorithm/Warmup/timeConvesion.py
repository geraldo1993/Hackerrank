#!/bin/python

import sys




time = raw_input().strip()
(h, m, rest) = time.split(':')

m = int(m)
h = int(h)

if rest.find('PM') != -1:
    timeFormat = "PM"
    if h >= 1 and h <= 11:
        h += 12
else:
    timeFormat = "AM"
    if h == 12:
        h = 0
        
rest = rest.replace(timeFormat, '')
h = '{:02}'.format(h)
m = '{:02}'.format(m)

time_convesion = str(h) + ":" + str(m) + ":" + rest
print(time_convesion)
