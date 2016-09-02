string = list(raw_input().strip())

i = 0
while i < len(string)-1:
    if string[i] == string[i+1]:
            del string[i]
            del string[i]
            i = 0
    else:
        i += 1
        
if len(string) > 0:
    print ''.join(string)
else:
    print 'Empty String'
