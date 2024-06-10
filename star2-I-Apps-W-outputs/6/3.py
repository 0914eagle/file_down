
def solve(s):
    n = len(s)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i-1] + 1
        for j in range(i):
            if s[j:i] == s[j:j+(i-j)]:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n]

n = int(input())
s = input()
print(solve(s))

