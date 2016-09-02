#!/bin/python

import sys

def compare_the_score(a, b):
    score_a = 0
    score_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1
    return score_a, score_b

a0,a1,a2 = raw_input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]

b0,b1,b2 = raw_input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]

print('%d %d' % compare_the_score(a,b))
