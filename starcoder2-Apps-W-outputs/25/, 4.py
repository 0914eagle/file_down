
# -*- coding: utf-8 -*-
# @Date    : 2019-03-10 16:20:32
# @Author  : zhangguangxun ()
# @Link    : https://github.com/zhangguangxun

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_str():
    return sys.stdin.readline().strip()

def read_strs():
    return sys.stdin.readline().split()

def print_list(l):
    print ' '.join(map(str, l))

def print_matrix(m):
    for i in range(len(m)):
        print_list(m[i])

def solve():
    n = read_int()
    W = []
    for i in range(n):
        W.append(list(read_ints()))

    A = [[0] * n for i in range(n)]
    B = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            A[i][j] = (W[i][j] + W[j][i]) / 2.0
            B[i][j] = (W[i][j] - W[j][i]) / 2.0
            A[j][i] = A[i][j]
            B[j][i] = -B[i][j]

    print_matrix(A)
    print_matrix(B)

if __name__ == '__main__':
    solve()
