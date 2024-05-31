
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_ways(n, numbers):
    MOD = 10**9 + 7
    factors = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if gcd(numbers[i], numbers[j]) > 1:
                factors[i].add(j)
                factors[j].add(i)

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][(i+1) % n] = 1

    for d in range(2, n):
        for i in range(n):
            j = (i + d) % n
            for k in factors[i]:
                dp[i][j] += dp[k][(j-1+n) % n]
                dp[i][j] %= MOD

    total_ways = sum(dp[i][(i-1+n) % n] for i in range(n)) % MOD
    return total_ways

# Read input
n = int(input())
numbers = [int(input()) for _ in range(n)]

# Calculate and output the number of ways
result = count_ways(n, numbers)
print(result)
