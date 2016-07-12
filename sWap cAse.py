# Enter your code here. Read input from STDIN. Print output to STDOUT

s=raw_input()
swap=""
for i in s:
    if i.isupper():
        swap+=i.lower()
    else:
        swap+=i.upper()
print swap
        
    
