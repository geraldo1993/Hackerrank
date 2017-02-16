n = input()
nums = map(int, input().split())
import collections
counter = collections.Counter(nums)
for i in range(0, 100):
    for j in range(counter[i]):
        print (i, end=" ")  
