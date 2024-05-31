
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_ways(n, numbers):
    mod = 10**9 + 7
    factors = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(numbers[i], numbers[j]) != 1:
                factors[i].add(j)
                factors[j].add(i)
    
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][(i+1) % n] = 1
    
    for length in range(2, n):
        for i in range(n):
            j = (i + length) % n
            for k in factors[j]:
                dp[i][j] = (dp[i][j] + dp[(i+1)%n][k]) % mod

    total_ways = sum(dp[i][i] for i in range(n)) % mod
    return total_ways

n = int(input())
numbers = [int(input()) for _ in range(n)]
ways = count_ways(n, numbers)
print(ways)
