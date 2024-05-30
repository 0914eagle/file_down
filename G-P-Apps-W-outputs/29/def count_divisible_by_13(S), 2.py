
def count_divisible_by_13(S):
    MOD = 10**9 + 7
    dp = [0] * 13
    dp[0] = 1

    for c in S:
        new_dp = [0] * 13
        if c == '?':
            for i in range(10):
                for j in range(13):
                    new_dp[(j*10 + i) % 13] += dp[j]
        else:
            for j in range(13):
                new_dp[(j*10 + int(c)) % 13] += dp[j]
        dp = [x % MOD for x in new_dp]

    return dp[5]

S = input().strip()
print(count_divisible_by_13(S))
```
