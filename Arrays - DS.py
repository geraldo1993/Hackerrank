#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.reverse()
for x in arr[:]: 
    print x,
