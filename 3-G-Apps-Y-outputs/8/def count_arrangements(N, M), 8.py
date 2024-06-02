
def count_arrangements(N, M):
    MOD = 10**9 + 7
    if abs(N - M) > 1:
        return 0
    
    fact = [1]
    for i in range(1, N + M + 1):
        fact.append((fact[-1] * i) % MOD)
    
    def mod_inv(x):
        return pow(x, MOD - 2, MOD)
    
    def nCr(n, r):
        return (fact[n] * mod_inv(fact[r]) * mod_inv(fact[n - r])) % MOD
    
    if N == M:
        return (2 * nCr(N, N) * nCr(M, M)) % MOD
    else:
        return (nCr(N + M, N) * nCr(N + M, M)) % MOD

N, M = map(int, input().split())
print(count_arrangements(N, M))
