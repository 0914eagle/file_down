
#encoding:utf-8
#https://codeforces.com/problemset/problem/1287/B
from collections import defaultdict

n,m = map(int, input().split())
a = list(map(int, input().split()))
res = 0
for i in range(1, m+1):
    for j in range(i+1, m+1):
        for k in range(n):
            if j & 1 == 0 and j/2 == a[k]:
                res += 1
            if (i+j) & 1 == 0 and (i+j)//2 == a[k]:
                res += 1
            if i == a[k] and j in a:
                res += 1
print(res)
