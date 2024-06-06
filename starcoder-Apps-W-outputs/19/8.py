
# -*- coding: utf-8 -*-
# @Author:             
# @Create Time:        2019-04-13 17:57:24
# @Update Time:        2019-04-13 17:57:24
# @Email:              

import os

os.sys.setrecursionlimit(1000000)
INF = 0x3f3f3f3f3f3f3f3f
from functools import reduce
from collections import Counter
from collections import defaultdict


def debug(*args):
    # print(*args)
    pass


def readint():
    return list(map(int, input().split()))


def readstrs():
    return input().split()


def readintlist():
    return list(map(int, input().split()))


def readstrlist():
    return input().split()


def main():
    b1, q, l, m = readint()
    bads = set(readintlist())
    debug(bads)
    cnt = 0
    while abs(b1) <= l and b1 not in bads:
        cnt += 1
        b1 *= q
    if cnt != 0:
        print(cnt)
    else:
        print("inf")


if __name__ == "__main__":
    main()

