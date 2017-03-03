def differenceL(a):
    a.sort()
    smallestDif=max
    smallestPair=[]
    for i in range(0,len(a)-1):
            difference=a[i+1]-a[i]
            if difference<smallestDif:
                smallestDif=difference
                smallestPair=[(a[i],a[i+1])]
            elif difference == smallestDif:
                smallestPair.append((a[i],a[i+1]))
    for i in smallestPair:
            print i[0],i[1],

            
            

n = int(raw_input().strip())
Set = map(int,raw_input().strip().split(' '))
differenceL(Set)
