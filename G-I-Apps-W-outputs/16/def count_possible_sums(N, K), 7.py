
def count_possible_sums(N, K):
    MOD = 10**9 + 7
    
    if K == 1:
        return (N+2) % MOD

    def powmod(a, b, mod):
        res = 1
        while b > 0:
            if b & 1:
                res = (res * a) % mod
            a = (a * a) % mod
            b >>= 1
        return res

    ans = 0
    for i in range(K, N+2):
        min_sum = powmod(10, 100, MOD) * 2 - 1
        max_sum = (10**100 + i - 1) + (10**100 + N - i + 1)
        cnt = max_sum - min_sum + 1
        ans += cnt
        ans %= MOD

    return ans

# Input handling
N, K = map(int, input().split())
print(count_possible_sums(N, K))
