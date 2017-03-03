#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
l=len(s)
les=n/len(s)
mod=n%len(s)
count=0
for i in range(0,l):
    if s[i]=='a':
        count+=1
res=count*les     
for i in range(0,mod):
    if s[i]=='a':
        res+=1
print res
        
   


