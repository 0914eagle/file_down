
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline

n = int(input())

theorem = [[] for i in range(n)]

for i in range(n):
    p = int(input())
    for j in range(p):
        l,k,l1 = map(int,input().split())
        l1 = sorted(l1)
        theorem[i].append((l,k,l1))

dp = [[[0 for j in range(n)] for i in range(n)] for k in range(1001)]

def solve(i,j,k):
    if(k == n):
        if(j == 0):
            return 0
        else:
            return 1e9
    if(dp[i][j][k] != 0):
        return dp[i][j][k]
    ans = 1e9
    for (l,k1,l1) in theorem[k]:
        if(k1 <= j):
            ans = min(ans,l + solve(i,j-k1,k1)+solve(i+l,j-k1,k+1))
    dp[i][j][k] = ans
    return ans

ans = solve(0,n-1,0)
print(ans)
