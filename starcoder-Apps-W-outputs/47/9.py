
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 22:49
# @Author  : Derek
# @Site    : 
# @File    : 1207B.py
# @Software: PyCharm
import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# 1. 输入
line1 = list(map(int, input().split(' ')))
n, m = line1[0], line1[1]
a_list = list(map(int, input().split(' ')))
b_list = list(map(int, input().split(' ')))
# 2. 处理
a_list.sort()
b_list.sort()
ans = a_list[0] * b_list[-1]

print(ans)

