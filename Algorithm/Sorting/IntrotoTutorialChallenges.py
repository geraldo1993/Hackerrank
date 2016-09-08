num= input()
n=input()
array=[int(x) for x in raw_input().split(" ")]

for i,x in enumerate(array):
    if x ==num:
        print i
