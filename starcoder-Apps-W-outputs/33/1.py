
# -*- coding: utf-8 -*-
# @Author: haonanwu
# @Date:   2017-06-27 18:30:30
# @Last Modified by:   haonanwu
# @Last Modified time: 2017-06-27 19:02:20
#
# 按题目要求打印输出，未进行整合。

n = int(raw_input())
data = []
for i in range(n):
	a = map(int, raw_input().split())
	data.append(a)

for i in range(1, n):
	for j in range(i):
		for x in data[i][1:]:
			if x in data[j][1:]:
				print data[i][0], data[j][0], x
				break

