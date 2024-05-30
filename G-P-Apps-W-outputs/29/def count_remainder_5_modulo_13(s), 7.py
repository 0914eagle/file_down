
def count_remainder_5_modulo_13(s):
    MOD = 10**9 + 7
    dp = [[0]*13 for _ in range(len(s)+1)]
    dp[0][0] = 1

    for i in range(len(s)):
        new_dp = [[0]*13 for _ in range(10)]
        for j in range(13):
            for d in range(10):
                if s[i] == '?' or s[i] == str(d):
                    for k in range(13):
                        new_dp[(j*10+d)%13][k] += dp[j][k]
                        new_dp[(j*10+d)%13][k] %= MOD
        dp = new_dp

    return dp[5][0]

S = input().strip()
print(count_remainder_5_modulo_13(S))
```
