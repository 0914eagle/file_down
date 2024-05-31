
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_sets(N):
    dp = [0] * (1 << N)
    dp[0] = 1

    for mask in range(1, 1 << N):
        size = bin(mask).count('1')
        for i in range(N):
            if mask & (1 << i):
                for j in range(i + 1, N):
                    if mask & (1 << j) and gcd(i + 1, j + 1) == 1:
                        dp[mask] += dp[mask ^ (1 << i) ^ (1 << j)]

    return dp[(1 << N) - 1] % 1000000000

# Input handling
N = int(input())
result = count_sets(N)
print(result)
