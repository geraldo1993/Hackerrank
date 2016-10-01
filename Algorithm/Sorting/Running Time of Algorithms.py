# Enter your code here. Read input from STDIN. Print output to STDOUT
def insertion_sort(list):
    counter=0
    for i in xrange(1,len(list)):
        value=list[i]
        pos=i-1
        while (pos>=0 and list[pos]>value):
            list[pos+1]=list[pos]
            list[pos]=value
            pos=pos-1
            counter=counter+1
    print counter        
       
    
m=int(raw_input())
list=[ int(x) for x in (raw_input().strip().split())]
insertion_sort(list)

         
