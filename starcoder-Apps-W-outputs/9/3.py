
# -*- coding: utf-8 -*-
# @Author: 
# @Date:   2019-02-08 19:45:35
# @Last Modified by:   
# @Last Modified time: 2019-02-08 19:49:01
# @Email: 

n, p = map(int, raw_input().split())

res = 0

for _ in xrange(n):
    if raw_input() == 'halfplus':
        res += p/2 + p/2

print res
