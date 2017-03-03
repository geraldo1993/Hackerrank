s1 = str(raw_input())
s2 = str(raw_input())


counter = 0
for i in range(len(s1)):
    if s1[i:].startswith(s2):
		counter += 1
print counter
