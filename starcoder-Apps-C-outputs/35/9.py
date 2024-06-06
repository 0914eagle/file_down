
# -*- coding:utf-8 -*-
# @Author: Wangmeng
# @Time: 2019/8/14 22:13
# @File: 686. Painting Square.py

n, m = list(map(int, input().split(' ')))

min_x = n
min_y = n
max_x = 0
max_y = 0

for i in range(m):
    x_i1, y_i1, x_i2, y_i2 = list(map(int, input().split(' ')))
    min_x = min(min_x, x_i1)
    min_y = min(min_y, y_i1)
    max_x = max(max_x, x_i2)
    max_y = max(max_y, y_i2)

res = 0
res += max_x - min_x + max_y - min_y
res += max(min_y - 1, n - max_y)
res += max(min_x - 1, n - max_x)
print(res)
