def equalSum(a):   
    
    low = 0
    high = len(a) - 1
     
    low_sum = a[low]
    high_sum = a[high]
     
    while low != high:
        if low_sum < high_sum:
            low += 1
            low_sum += a[low]
        else:
            high -= 1
            high_sum += a[high]
     
    return low_sum == high_sum
     
if __name__ == '__main__':
    n = int(raw_input())
    for _ in xrange(n):
        n = int(raw_input())
        a = map(int, raw_input().split())
        if equalSum(a):
            print "YES"
        else:
            print "NO"
