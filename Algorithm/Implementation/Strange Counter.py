#!/bin/python
'''we know the initial values of time and value are 1 and 3 respectively. You were also told that at each step the 
value gets doubled. Look at the example and you'll see that the next counter starts at time + value.If you look carefully, the last 'time' value of cycle 1 is 3 which is 3*1=3*(2^1-1), the last 'time' value of cycle 2 is 9 which is 3*3=3*(2^2-1), the last 'time' value of cycle 3 is 21 which is 3*7=3*(2^3-1).
So, we should keep doubling n, which represents the 2^1, 2^2, 2^3 part. Hence the while loop. The loop stops when it reaches to a cycle whose max time is bigger than the real time t, then we know that it has reached the last cycle.
And taking the second cycle as an example, 'time' 7 has 'value' 3, and the max time of the second cycle is 9. We find the relationship between them is 3 = 9 - 7 + 1, which is why we print (3 * (n - 1) - t + 1) to get the output of 3 when t is 7.'''


import sys
t = int(raw_input().strip())
value = 3
while t > value:
    t = t-value
    value *= 2

print(value-t+1)
