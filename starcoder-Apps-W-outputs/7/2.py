
from itertools import permutations as perm
import sys
import math
from collections import deque

def prime(n):
    if n % 2 == 0: return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def main():
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())

    l = []
    for i in range(1,a+1):
        for j in range(1,b+1):
            l.append((i,j))
    res = 0
    for i in perm(l,c):
        res += dist(i)
    print(res)
    for i in l:
        print(i,end=' ')
    print()


def dist(l):
    d = 0
    for i in range(len(l)-1):
        d += abs(l[i][0] - l[i+1][0]) + abs(l[i][1] - l[i+1][1])
    return d

main()

