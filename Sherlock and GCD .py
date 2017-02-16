def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
def multiple_gcd(numbers):
    return reduce(lambda x,y: gcd(x,y), numbers)
 
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        n = input()
        values = map(int, raw_input().split())
        if len(values) < 2:
            print "NO"
            continue
        if (multiple_gcd(values) == 1):
            print "YES"
        else:
            print "NO"
