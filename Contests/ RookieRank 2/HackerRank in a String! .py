
#https://www.hackerrank.com/contests/rookierank-2/challenges/hackerrank-in-a-string/submissions/code/1300466674

#!/bin/python3

import sys

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    Geraldo=""
    for letter in "hackerrank":
        if letter in s:

            s=s[s.find(letter)+1:]
            Geraldo+=letter
        else:
            print("NO")
            break
            continue

        if Geraldo=="hackerrank":
            print("YES")
