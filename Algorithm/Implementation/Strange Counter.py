#!/bin/python
'''we know the initial values of time and value are 1 and 3 respectively. You were also told that at each step the 
value gets doubled. Look at the example and you'll see that the next counter starts at time + value.'''


import sys
t = int(raw_input().strip())
value = 3
while t > value:
    t = t-value
    value *= 2

print(value-t+1)
