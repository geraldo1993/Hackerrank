#!/bin/python

import sys
def diagonal(x):
    i = 0
    matrix = [[],[]]
    while i < len(x):
        matrix[0].append(x[i][i])
        matrix[1].append(x[i][-i - 1])
        i += 1
    return abs(sum(matrix[0])-sum(matrix[1]))

prova_mundesite = int(raw_input().strip())
vlera = []
for _ in range(prova_mundesite):
    vlera.append([int(num) for num in raw_input().strip().split()])
print diagonal(vlera)
