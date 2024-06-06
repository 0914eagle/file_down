
# coding:utf-8

a, b = map(str, input().split())

for i in range(len(a)):
    for j in range(len(b)):
        print(a[:i+1] + b[:j+1])
