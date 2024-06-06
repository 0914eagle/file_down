
s = input()
n = len(s)

dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if s[j] < s[i]:
            dp[i] += dp[j]
print(sum(dp))
