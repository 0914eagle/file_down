
import sys,string,math

from sys import stdin as s

n = int(s.readline())

a = [int(x) for x in s.readline().split()]

b = [int(x) for x in s.readline().split()]

A = []

for i in range(n):

    A.append((a[i],b[i]))

A.sort()

ans = []

for i in range(n):

    ans.append(A[i][1])

print(len(ans),sum(ans))
