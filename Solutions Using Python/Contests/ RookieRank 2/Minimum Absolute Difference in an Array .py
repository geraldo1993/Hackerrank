
#https://www.hackerrank.com/contests/rookierank-2/challenges/minimum-absolute-difference-in-an-array/submissions/code/1300467595
#!/bin/python3

import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# your code goes here
a.sort()
min=[]
for i in range(len(a)):
    min.append( abs((a[i]-a[i-1])))
    i+=1
min.sort()



print (min[0])
