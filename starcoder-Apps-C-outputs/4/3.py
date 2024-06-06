
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


N = int(input())
ab = []
for i in range(2*N):
    a = input().split()
    ab.append((a[0],a[1]))

a = sorted(ab[:N], key=lambda x: int(x[1]))
b = sorted(ab[N:], key=lambda x: int(x[1]))

sw = []
for i in range(N):
    if a[i][1] != b[i][1]:
        sw.append(i)
        
print(len(sw))
