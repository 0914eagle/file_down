
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_ways(n, numbers):
    MOD = 10**9 + 7
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            if gcd(numbers[i], numbers[j]) > 1:
                dp[i][j] = 1
    
    for d in range(2, n):
        for i in range(n):
            j = (i + d) % n
            for k in range(i, j):
                dp[i][j] = (dp[i][j] + dp[i][k] * dp[(k+1) % n][j]) % MOD
    
    return dp[0][-1]

# Read input
n = int(input())
numbers = [int(input()) for _ in range(n)]

# Calculate and output the result modulo 10^9 + 7
result = count_ways(n, numbers) % (10**9 + 7)
print(result)
