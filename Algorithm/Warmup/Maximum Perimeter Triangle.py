n = int(input())
A = sorted(int(i) for i in input().split())

i = n-3
while i >= 0 and (A[i] + A[i+1] <= A[i+2]) :
    i -= 1

if i >= 0 :
    print(A[i],A[i+1],A[i+2])
else :
    print(-1)
