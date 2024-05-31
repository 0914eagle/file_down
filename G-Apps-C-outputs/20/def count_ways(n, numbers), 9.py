
from math import gcd
MOD = 10**9 + 7

def count_ways(n, numbers):
    def factors(num):
        result = set()
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                result.add(i)
                result.add(num // i)
        result.add(num)
        return result

    factors_list = [factors(num) for num in numbers]
    
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for length in range(2, n + 1):
        for i in range(n):
            j = (i + length - 1) % n
            if gcd(numbers[i], numbers[j]) > 1:
                dp[i][j] = sum(dp[(i+k) % n][(j-k) % n] for k in range(1, length)) % MOD
    
    total_ways = sum(dp[i][(i-1) % n] for i in range(n)) % MOD
    return total_ways

# Read input
n = int(input())
numbers = [int(input()) for _ in range(n)]

# Calculate and output the result
result = count_ways(n, numbers)
print(result)
