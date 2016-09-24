#!/bin/python

import sys


s = raw_input().strip()
s1=1
for i in s:
    if i.isupper()==True:
        s1+=1

print s1

