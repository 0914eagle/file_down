
# -*- coding: utf-8 -*-
# @Author: 
# @Date:   2019-08-06 19:49:45
# @Last Modified by:   
# @Last Modified time: 2019-08-06 20:15:32

# 10^9+9是质数，所以可以直接求逆元
# 10^9+9=10^3*10^3+9=10^3*10^3+3*10^3+6*10^3+3
# 10^9+9的逆元是10^6+10^3+1

n,a,b,k=map(int,input().split())
s=input()

if s=='-':
    print((a**n-b**n)%(10**9+9))
else:
    if n%2==0:
        print((a**n+b**n)%(10**9+9))
    else:
        print((a**n-b**n)%(10**9+9))
