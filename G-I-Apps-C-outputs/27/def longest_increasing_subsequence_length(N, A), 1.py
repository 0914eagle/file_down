
def longest_increasing_subsequence_length(N, A):
    MOD = 1000000007
    fact = [1]
    for i in range(1, max(A) + 2):
        fact.append((fact[-1] * i) % MOD)

    inv_fact = [None] * (max(A) + 2)
    inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(max(A), 0, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    def nCr(n, r):
        return (fact[n] * inv_fact[r] * inv_fact[n - r]) % MOD

    def cnt(arr):
        n = len(arr)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = (dp[i] + dp[j]) % MOD
        return dp[-1]

    answer = 0
    for i in range(N):
        answer += cnt(list(range(1, A[i] + 1)))
    
    return answer * pow(len(A), MOD - 2, MOD) % MOD

N = int(input())
A = list(map(int, input().split()))
print(longest_increasing_subsequence_length(N, A))
```
