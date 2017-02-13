#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]


array = sorted([a,b,c,d,e])
max,min,sum =0,0,0
for i in range(1,len(array)-1):
    sum = sum+ array[i]
max = sum+array[-1]
min = sum+array[0]
print(str(min)+' '+str(max))
