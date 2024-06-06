
# -*- coding: utf-8 -*-
# @Author: 
# @Date:   2019-05-13 14:52:35
# @Last Modified by:   
# @Last Modified time: 2019-05-13 14:52:35

t = int(input())
for i in range(t):
    k = int(input())
    s = input()
    count = 0
    for j in range(k):
        if s[j] == 'A':
            count += 1
    print(count)
