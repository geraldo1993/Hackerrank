
import sys


n = int(raw_input().strip())
B = raw_input().strip()

count = 0
i = 0
while i <= n-3:
    if "010" == B[i:i+3]:
        count += 1
        i += 3
    else:
        i += 1

print(count)
