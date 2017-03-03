#!/bin/python

import sys


n = float(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
countNegative=0
countPositive=0
countZero=0
if((len(arr))==n):
    for i in (arr):
        if((int(i))>0):
            countPositive=countPositive+1
        elif((int(i))<0):
            countNegative=countNegative+1
        else:
            countZero=countZero +1

positive = float(countPositive/n)
negative = float(countNegative/n)
zero= float(countZero/n)

print (positive) 
print negative
print zero
 
