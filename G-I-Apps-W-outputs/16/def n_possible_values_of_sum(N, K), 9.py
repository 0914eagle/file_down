
MOD = 10**9 + 7

def n_possible_values_of_sum(N, K):
    ans = 0
    for i in range(K, N+2):
        min_sum = (10**100) * i + (i * (i - 1)) // 2
        max_sum = (10**100 + N) * i - (i * (i - 1)) // 2
        ans += (max_sum - min_sum + 1) % MOD
    return ans

# Input handling
N, K = map(int, input().split())

result = n_possible_values_of_sum(N, K)
print(result % MOD)
```
