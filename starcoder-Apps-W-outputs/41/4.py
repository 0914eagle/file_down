
# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
res = 0
for i in range(1, 101):
    if a.count(i) >= n:
        res += 1
print res
