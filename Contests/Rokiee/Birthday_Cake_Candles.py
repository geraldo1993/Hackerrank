#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))
counter=0
max=-1000000
for i in height:
     if max<i:
        max=i
        
for i in height:
        if i==max:
            counter+=1
print counter



