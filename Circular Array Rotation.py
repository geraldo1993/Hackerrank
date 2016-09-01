#!/usr/bin/py
if __name__ == '__main__':
    n,k,q = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    for _ in xrange(q):
        x = int(raw_input())
        print arr[(x-k)%n]
