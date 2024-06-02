
MOD = 10**9 + 7

def count_subsequences(n, m):
    result = 1
    for i in range(1, n+1):
        result = (result * (m + 1) - 1) % MOD
    return result

n, m = map(int, input().split())
print(count_subsequences(n, m))
