#!/bin/python

import sys

arr = [[0 for x in range(6)] for x in range(6)]
for j in range(0,6):
    arr1 = [int(i) for i in raw_input().strip().split()]
    for k in range(0,6):
        arr[j][k] = arr1[k] 

sum = -100        
for i in range(0,4):
    for j in range(0,4):
        count = 0
        count = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if(count >= sum):
            sum = count
        
print sum
