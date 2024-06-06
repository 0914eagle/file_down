
# coding:utf-8

import numpy as np
import copy

def min_article(n, data):
    # data = {i: [] for i in range(n)}
    # for i in range(n):
    #     p_i = int(input())
    #     for _ in range(p_i):
    #         info = input().split()
    #         data[i].append([int(info[0]), [int(x) for x in info[2:]]])
    # print(data)
    dp = np.zeros((n, 1), dtype=int)
    dp[0] = np.min(data[0])
    print(dp)
    for i in range(1, n):
        for p_i in range(len(data[i])):
            dp[i] = min(dp[i], data[i][p_i][0] + np.min([dp[d_i] for d_i in data[i][p_i][1:]]))
    return dp

if __name__ == '__main__':
    n = int(input())
    data = {i: [] for i in range(n)}
    for i in range(n):
        p_i = int(input())
        for _ in range(p_i):
            info = input().split()
            data[i].append([int(info[0]), [int(x) for x in info[2:]]])
    # print(data)
    print(min_article(n, data))
