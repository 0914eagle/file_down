
MOD = 10**9 + 7

def count_special_numbers(n, k):
    dp = [0] * 1005
    dp[1] = 1
    
    def count_set_bits(x):
        count = 0
        while x:
            count += 1
            x &= x - 1
        return count
    
    for i in range(1, n + 1):
        cnt = count_set_bits(i)
        for j in range(1, k + 1):
            dp[cnt] += dp[j]
            dp[cnt] %= MOD
            
    return sum(dp[1:k+1]) % MOD

n = int(input(), 2)
k = int(input())
print(count_special_numbers(n, k))
```
