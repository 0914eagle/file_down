
# https://github.com/stevenhalim/cpbook-code/blob/master/ch3/parentheses.py
from sys import stdin
def f(n, k):
    global s, c, sum_
    # print(n, k)
    if n == 0:
        return 0
    if k == 0:
        return float("inf")
    if dp[n][k] != -1:
        return dp[n][k]
    dp[n][k] = float("inf")
    if s[n-1] == '(':
        dp[n][k] = min(dp[n][k], f(n-1, k-1)+c[n-1])
        dp[n][k] = min(dp[n][k], f(n-1, k)+sum_-sum_[n-1])
    elif s[n-1] == ')':
        dp[n][k] = min(dp[n][k], f(n-1, k-1)-c[n-1])
        dp[n][k] = min(dp[n][k], f(n-1, k)-sum_+sum_[n-1])
    # print(dp[n][k])
    return dp[n][k]

for _ in range(1):
    n, k = map(int, stdin.readline().strip().split())
    s = stdin.readline().strip()
    c = [int(stdin.readline().strip()) for _ in range(n)]
    sum_ = [0 for _ in range(n+1)]
    for i in range(n):
        sum_[i+1] = sum_[i]+c[i]
    dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]
    print(f(n, k))
