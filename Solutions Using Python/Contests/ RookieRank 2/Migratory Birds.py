#https://www.hackerrank.com/contests/rookierank-2/challenges/migratory-birds/submissions/code/1300467876
#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here
from collections import Counter
c=Counter(types)
print (sorted(list(c.items()),key=lambda x: (-x[1],x[0]))[0][0])
