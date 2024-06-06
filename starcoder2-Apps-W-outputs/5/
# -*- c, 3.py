
# -*- coding: utf-8 -*-
# @Author: 
# @Date:   2019-03-08 17:29:48
# @Last Modified by:   
# @Last Modified time: 2019-03-08 17:30:07

x, y, a, b = map(int, input().split())

if a > x or b > y:
    print(0)
else:
    print(x - a + 1)
    for i in range(a, x + 1):
        print(i, y)
