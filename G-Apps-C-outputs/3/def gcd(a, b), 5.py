
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_sets(N):
    dp = [[0 for _ in range(1 << N)] for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for mask in range(1 << N):
            for j in range(i):
                if mask & (1 << j) == 0 and gcd(i, j + 1) == 1:
                    dp[i][mask | (1 << j)] += dp[i - 1][mask]
    
    return sum(dp[N])

N = int(input().strip())
result = count_sets(N) % 1000000000
print(result)
