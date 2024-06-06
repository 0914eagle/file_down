
# -*- coding: utf-8 -*-
# @Author: 
# @Date:   2018-05-19 11:58:07
# @Last Modified by:   
# @Last Modified time: 2018-05-19 12:06:27

t = int(input())
for i in range(t):
    k = int(input())
    s = input()
    count = 0
    for j in range(k):
        if s[j] == 'P':
            count += 1
        else:
            break
    print(count)
