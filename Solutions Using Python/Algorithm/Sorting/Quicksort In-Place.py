m = input()
ar = [int(i) for i in input().strip().split()]


def print_array(ar):
    st = ""
    for i in range(0, len(ar)):
        st += str(ar[i])+" "
    print (st)
        
        
def exchange(ar, i, j):
    tmp = ar[i]
    ar[i] = ar[j]
    ar[j] = tmp
    return ar
    
def partition(ar, p , r):
    x = ar[r]
    i = p-1
    for j in range(p,r):
        if(ar[j] <= x):
            i += 1
            ar = exchange(ar, i, j)
    ar = exchange(ar, i+1, r)
    print_array(ar)
    return [i+1, ar]

def quicksort(ar, p, r):
    if(p < r):
        L = partition(ar, p, r)
        q = L[0]
        ar = L[1]
        quicksort(ar, p, q-1)
        quicksort(ar,q+1, r)
    return ar
        
quicksort(ar, 0, len(ar)-1)
