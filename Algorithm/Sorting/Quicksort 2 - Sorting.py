n=int(input())
arr=[int(x) for x in input().strip().split()]

def quickSort(ar):
    if len(ar)<=1:
        return(ar)
    else:
        left=[]
        right=[]
        middle=[]
        middle.append(ar[0])
    for i in range(1,len(ar)):
        if ar[i]<middle[0]:
            left.append(ar[i])
        else:
            right.append(ar[i])
    newarr=quickSort(left)+middle+quickSort(right)
    par=[str(x) for x in newarr]
    print(' '.join(par))
    return(newarr)
quickSort(arr)
