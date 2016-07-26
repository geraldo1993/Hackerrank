# Enter your code here. Read input from STDIN. Print output to STDOUT

L=[]
num=int (raw_input())
for i in range(0,num):
    arr=raw_input().split();
    if arr[0] == "insert":
        L.insert(int(arr[1]),int(arr[2]))
    elif arr[0] == "append":
        L.append(int(arr[1]))
    elif arr[0] == "pop":
        L.pop();
    elif arr[0] == "print":
        print L
    elif arr[0] == "remove":
        L.remove(int(arr[1]))
    elif arr[0] == "sort":
        L.sort();
    else:
        L.reverse();

