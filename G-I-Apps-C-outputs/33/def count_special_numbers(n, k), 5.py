
def count_special_numbers(n, k):
    dp = [[0] * (k + 1) for _ in range(len(n) + 1)]
    dp[0][0] = 1
    
    for i in range(1, len(n) + 1):
        for j in range(k + 1):
            for x in range(2):
                if x == 1:
                    dp[i][j] += dp[i-1][j-1] % (10**9 + 7)
                else:
                    dp[i][j] += dp[i-1][j] % (10**9 + 7)
    
    result = sum(dp[-1])
    return result % (10**9 + 7)

n = input().strip()
k = int(input().strip())
print(count_special_numbers(n, k))
```
