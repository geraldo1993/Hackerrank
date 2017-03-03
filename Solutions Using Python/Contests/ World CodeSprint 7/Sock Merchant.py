#!/bin/python

import sys
import collections

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
my_s=[]
for i in list(set(c)):
    my_s.append(c.count(i))
total=0
for i in my_s:
    if i >1:
        i=i/2
        total+=i
print total




