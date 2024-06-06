
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 15:13:47
# @Author  :  ()
# @Link    : link
# @Version : 1.0.0

from sys import stdin

maxn = 180
maxc = 10 ** 9

def read():
    return map(int, stdin.readline().split())

def write(x):
    print(x)

def solve():
    n = int(input())
    W = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        W[i] = list(map(int, input().split()))
    A = [[0 for i in range(n)] for j in range(n)]
    B = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = (W[i][j] + W[j][i]) / 2
            B[i][j] = (W[i][j] - W[j][i]) / 2
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print(B[i][j], end=' ')
        print()

if __name__ == '__main__':
    solve()
