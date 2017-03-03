#!/bin/python
def partition(arr):
    
    pivot = arr[0]
    
    left=[]
    
    right=[]
    
    for i in arr:
        
        if i >=pivot:
            
            right.append(i)
        
        elif i<pivot:
            
            left.append(i)
    for a in left:
        
        print(a, end=" ")
    for t in right:
        print(t, end=" ")
    return ""

m = input()
arr = [int(i) for i in input().strip().split()]
partition(arr)
            
            
        
        
    
        
        
    


