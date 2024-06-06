
# -*- coding: utf-8 -*-

# @Date: 2019-03-11 11:55:38
# @Author: Huangstaryuan ()
# @GitHub: https://github.com/Huangstaryuan

n = int(input())
a = []
b = []
for i in range(n):
    x,y,z = map(int,input().split())
    a.append(x)
    b.append(y)
a.sort()
b.sort()
for i in range(n//2):
    print(i+1,n-i)

