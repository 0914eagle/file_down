
# -*- coding: utf-8 -*-
# @Date    : 2018-11-15 21:06:15
# @Author  : cbookgz ()
# @Github  : https://github.com/cbookgz
# @Link    : https://cbookgz.github.io/
# @Version : $Id$

import sys

sys.setrecursionlimit(1000000)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def solve(n, arr):
    

    def f(i, s):
        if dp[i] is not None:
            return dp[i]
        if s == arr[i]:
            dp[i] = 1
            return 1
        if s.startswith(arr[i]) and s.endswith(arr[i]):
            dp[i] = 1 + f(i, s[len(arr[i]):])
            return dp[i]
        else:
            dp[i] = 0
            return 0

    dp = [None] * n
    for i in range(n):
        f(i, arr[i])
    return max(dp)


if __name__ == '__main__':
    n = int(readline())
    arr = [readline().strip().decode('utf-8') for _ in range(n)]
    print(solve(n, arr))
