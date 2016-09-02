import numpy
a,b = map(int,raw_input().split())
arr = []
for _ in range(a):
    arr.append(map(int,raw_input().split()))
print numpy.max(numpy.min(numpy.array(arr), axis=1))
