
# -*- coding: utf-8 -*-


import numpy as np

n = int(input())

W = np.zeros((n,n))

for i in range(n):
    W[i] = list(map(int,input().split()))

A = np.zeros((n,n))
B = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        A[i][j] = (W[i][j] + W[j][i])/2
        B[i][j] = (W[i][j] - W[j][i])/2

for i in range(n):
    for j in range(n):
        print(A[i][j],end = ' ')
    print()

for i in range(n):
    for j in range(n):
        print(B[i][j],end = ' ')
    print()
