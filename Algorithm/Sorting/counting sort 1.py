n = int(input())
l = [0]*100
for i in map(int,input().split()):
    l[i]+=1
print(*l)
