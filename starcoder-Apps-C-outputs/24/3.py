
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 21:54
# @Author  : Lynn
# @Site    : 
# @File    : 1115. A Simple Task.py
# @Software: PyCharm

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))

count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == "E":
            arr[i][j] = "."
            for k in range(n):
                if arr[k][j] == "E":
                    arr[k][j] = "."
            for k in range(n):
                if arr[i][k] == "E":
                    arr[i][k] = "."
            count += 1

for i in range(n):
    if "E" in arr[i]:
        count = -1
        break
print(count)
for i in range(count):
    print(i + 1, i + 1)
