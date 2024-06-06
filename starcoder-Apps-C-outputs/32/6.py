
#coding=utf-8
# 前缀和
s = input()
a = s.count('a')
b = s.count('b')
c = s.count('c')
if a == b or a == c or b == c or (a == b and b == c):
    print('YES')
else:
    print('NO')
