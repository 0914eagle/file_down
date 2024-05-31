
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_sets(N):
    dp = [[0 for _ in range(N+1)] for _ in range(1<<N)]
    dp[0][0] = 1

    for mask in range(1 << N):
        for i in range(N):
            if ((mask >> i) & 1):
                for j in range(i + 1, N):
                    if ((mask >> j) & 1) == 0 and gcd(i+1, j+1) == 1:
                        dp[mask | (1 << j)][j] += dp[mask][i]

    total = sum(dp[(1<<N)-1])
    return total % 1000000000

# Read input
N = int(input().strip())

# Call count_sets function and print the result
print(count_sets(N))
