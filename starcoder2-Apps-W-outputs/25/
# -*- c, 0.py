
# -*- coding: utf-8 -*-


import numpy as np

n = int(input())
W = np.zeros((n,n))

for i in range(n):
    W[i] = np.array(input().split(), dtype = float)

A = np.zeros((n,n))
B = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        A[i,j] = (W[i,j] + W[j,i])/2
        B[i,j] = (W[i,j] - W[j,i])/2

print(A)
print(B)
