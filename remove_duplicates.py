def removeDuplicates(string):
    uniqs = ''
    for x in string:
        if not(x in uniqs):
            uniqs = uniqs + x
    return uniqs


print removeDuplicates('aaabccddd')
print removeDuplicates("baab")
