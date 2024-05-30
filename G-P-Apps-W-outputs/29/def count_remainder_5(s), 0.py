
def count_remainder_5(s):
    MOD = 1000000007
    dp = [0] * 13
    dp[0] = 1

    for char in s:
        new_dp = [0] * 13
        if char == '?':
            for i in range(10):
                for j in range(13):
                    new_dp[(j*10 + i) % 13] += dp[j]
                    new_dp[(j*10 + i) % 13] %= MOD
        else:
            for j in range(13):
                new_dp[(j*10 + int(char)) % 13] += dp[j]
                new_dp[(j*10 + int(char)) % 13] %= MOD
        dp = new_dp

    return dp[5]

S = input().strip()
print(count_remainder_5(S))
```
