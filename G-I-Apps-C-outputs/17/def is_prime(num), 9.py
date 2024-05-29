
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_prime_divisor(arr):
    max_prime_divisor = 0
    for num in arr:
        if is_prime(num):
            max_prime_divisor = max(max_prime_divisor, num)
    return max_prime_divisor

def max_score_partition(n, k, arr):
    dp = [[0 for _ in range(n)] for _ in range(k)]
    for i in range(n):
        dp[0][i] = find_largest_prime_divisor(arr[:i+1])

    for i in range(1, k):
        for j in range(i, n):
            dp[i][j] = dp[0][j]
            for x in range(1, j):
                dp[i][j] = min(dp[i][j], max(dp[i-1][x], find_largest_prime_divisor(arr[x+1:j+1])))

    return dp[-1][-1]

# Read input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Calculate and print the maximum score possible
print(max_score_partition(n, k, arr))
```
