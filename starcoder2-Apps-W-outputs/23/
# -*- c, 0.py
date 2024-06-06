
# -*- coding: utf-8 -*-
# @Author: 
# @Date:   2018-09-10 14:48:04
# @Last Modified by:   
# @Last Modified time: 2018-09-10 15:18:56

x, y, x0, y0 = map(int, input().split())
s = input()

# 左右上下
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 方向
d = {'L': 0, 'R': 1, 'U': 2, 'D': 3}

# 记录
cnt = [0] * (len(s) + 1)

# 初始坐标
x, y = x0, y0

for i in range(len(s)):
    # 移动
    x += dx[d[s[i]]]
    y += dy[d[s[i]]]

    # 越界
    if x < 1 or x > x or y < 1 or y > y:
        cnt[i + 1] = cnt[i]
        continue

    # 记录
    cnt[i + 1] = cnt[i] + 1

print(*cnt)
