
# coding:utf-8
# author:yuukisei
# filename:1468.py
# date:2019-04-21

import sys
import re


def input():
    return sys.stdin.readline().rstrip("\r\n")


def main():
    re_rule = re.compile(r"(\d+)")
    L, D, n = map(int, re_rule.findall(input()))
    birds = [0 for i in range(n)]
    for i in range(n):
        birds[i] = int(input())
    birds.sort()
    max_num = 0
    for i in range(n):
        if i == 0:
            max_num = max(max_num, birds[i] - 6)
            continue
        max_num = max(max_num, (birds[i] - birds[i-1]) // 2)
    max_num = max(max_num, (L - birds[n-1]) - 6)
    print(max_num - D + 1)


if __name__ == '__main__':
    main()
