import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if x1==x2 and v1==v2:
    print('YES')
if (x1==x2) and (v1>v2):
        print('NO')
if x1<x2 and v1<v2:
    print ('NO')
else:
    if (x2 - x1) % (v1 - v2) == 0 :
         print ("YES")
    else:
        print ('N0')
