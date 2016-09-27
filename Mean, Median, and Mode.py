# Enter your code here. Read input from STDIN. Print output to STDOUT
def mean(data_set):
    return float(sum(data_set)/float(n))


def median(data_set):
    data_set = sorted(data_set)
    if len(data_set) < 1:
            return None
    if len(data_set) %2 == 1:
            return data_set[((len(data_set)+1)/2)-1]
    else:
            return float(sum(data_set[(len(data_set)/2)-1:(len(data_set)/2)+1]))/2.0
        

def mode(data_set): 
    data_set.sort() 
    mode_count = 0 
    modes = 0 
    for item in data_set: 
        if data_set.count(item)>mode_count: 
            mode_count = data_set.count(item) 
            modes = item 
    return modes






n = int(raw_input().strip())
data_set = map(int,raw_input().strip().split(' '))
data_set.sort()

print mean(data_set)
print median(data_set)
print mode(data_set)


