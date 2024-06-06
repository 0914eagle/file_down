
'''
题意
输入数组a和x,k,求满足(ai<=y<=aj and y%x==0)有k个的(i,j)个数
思路
按照ai%x==0,分别把所有ai%x==0的分为两类,再分别统计在这两类里面满足条件的(i,j)个数
'''
import sys
import os
from sys import stdin
from sys import stdout
from collections import defaultdict
import math
import bisect
from decimal import *
from itertools import permutations
from math import sqrt
MAX = 10**9+10000

def getints(): return map(int, stdin.readline().split())
def getlist(): return list(getints())
def getlists(n): return [getlist() for _ in range(n)]
def getstr(): return list(stdin.readline().rstrip())
def getstrs(n): return [getstr() for _ in range(n)]

'''
input
5 2 2
1 1 2 3 4
output
2
'''

def getans(a,x,k):
    n=len(a)
    mod_0=[]
    mod_1=[]
    for i in range(n):
        if a[i]%x==0:
            mod_0.append(i)
        else:
            mod_1.append(i)
    ans=0
    if k==0:
        ans=len(mod_0)*len(mod_1)
    else:
        for i in mod_0:
            for j in mod_1:
                if j>i:
                    if (a[j]-a[i])%x==0:
                        ans+=1
    return ans

if __name__ == '__main__':
    n,x,k=getints()
    a=getlist()
    print(getans(a,x,k))
