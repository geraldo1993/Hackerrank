t = int(input())
for i in range(t):
    n,m,s = input().split()
    n,m,s = [int(n), int(m), int(s)]
    ans = (m+s-1)%n
    if ans==0:
        print(n)
    else:
        print(ans)

