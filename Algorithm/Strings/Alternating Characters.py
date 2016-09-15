# Enter your code here. Read input from STDIN. Print output to STDOUT
def Delete(s):
    stringToDelete=0
    if len(s)== 1:
         return 1
    for i in xrange(len(s)-1):
        if s[i]== s[i+1]:
            stringToDelete+=1
            
    return stringToDelete

n=input()

for x in range(n):
    string=(raw_input())
    print Delete(string)
    
    
