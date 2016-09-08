# Enter your code here. Read input from STDIN. Print output to STDOUT

t0, t1, n = map(int, raw_input().strip().split(' '))

for i in xrange(n-2):
    t1, t0 = t0 + t1*t1, t1

print(t1)
