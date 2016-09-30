#!/bin/python
def insertionSort(list):
    
    for i in xrange(1,len(list)):
        value=list[i]
        pos=i
        while pos>0 and value <list[pos-1]:           
            list[pos]=list[pos-1]
            list_ = map(str, list)
            print " ".join(list_)
            pos-=1
        list[pos]=value
        list_ = map(str, list)
    return " ".join(list_)
m = input()
list = [int(i) for i in raw_input().strip().split()]
print insertionSort(list)

