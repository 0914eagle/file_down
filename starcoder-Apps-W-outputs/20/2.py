
# -*- coding: utf-8 -*-
# @Date    : 2018-12-23 15:22:19
# @Author  : cbook
# @Version : 1.0

# 测试样例
# 22 2 2
# 11
# 9

length, dist, num = map(int, input().split())

blist = []
for i in range(num):
    blist.append(int(input()))

blist.sort()

count = 0
for i in range(1, len(blist)):
    if blist[i] - blist[i-1] <= dist:
        count += 1

print(len(blist)+count)
