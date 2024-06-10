
def solve(n, ops):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for a, b in ops:
            if i >= 2 and a == 'a' + b:
                dp[i] += dp[i-2]
            elif i >= 1 and a[0] == b:
                dp[i] += dp[i-1]
    return dp[n]

n, q = map(int, input().split())
ops = [input().split() for _ in range(q)]
print(solve(n, ops))

