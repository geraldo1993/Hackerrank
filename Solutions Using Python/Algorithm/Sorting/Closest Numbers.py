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










" First we sort and then check the diff of two adjecent numbers.. keep tracking the min value, update the both pairs in a list, if the new pair is having less than last min value, then delete the list, update with new pairs,, if the new pair is having exact value, add them in list too."

# first we get the input from the user
n =  input()
#here we are mapping and strippin the input into a list.
nums = list(map(int,input().strip().split()))
#from the build function here we are sorting the inputs
nums.sort()
lowestDiff = nums[1]-nums[0]
res = [nums[0],nums[1]]
for i in range(1,len(nums)-1):            
    if nums[i+1]-nums[i] < lowestDiff:
        res = []   
        res.append(nums[i])
        res.append(nums[i+1])
        lowestDiff = abs(nums[i+1]-nums[i])
    elif nums[i+1]-nums[i] == lowestDiff:

        #appending the list
        res.append(nums[i])
        res.append(nums[i+1])
#and at the end we are printing the result
print(*res)

