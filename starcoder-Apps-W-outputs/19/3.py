
'''
思路：
因为b1和q可以为0，所以可能无穷大，那么就是先判断是否无穷大。
然后再去寻找a1到am中在[b1-l,b1+l]中的个数
'''
# -*- coding: utf-8 -*-
# @Date    : 2019-02-16 14:34:14
# @Author  : zhangxuan
import math

b1, q, l, m = map(int, input().split())
a = [int(i) for i in input().split()]

def first(b1, q, l):
    if b1 == 0:
        return math.inf
    if q == 0:
        if abs(b1) <= l:
            return 1
        else:
            return 0
    else:
        if abs(b1) <= l:
            m1 = (l-b1)//abs(q)+1
            m2 = (l+b1)//abs(q)+1
            return max(m1, m2)
        else:
            return 0


print(first(b1, q, l))

