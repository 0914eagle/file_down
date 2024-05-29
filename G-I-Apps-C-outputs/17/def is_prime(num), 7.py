
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_divisor(arr):
    max_prime = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if is_prime(arr[j]):
                max_prime[i] = max(max_prime[i], arr[j])
    return max_prime

def max_score_partition(n, k, arr):
    max_prime = largest_prime_divisor(arr)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            for x in range(i):
                dp[i][j] = min(dp[i][j], max(dp[x][j - 1], max_prime[x]))

    return dp[n][k]

# Read input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Get the maximum score possible
print(max_score_partition(n, k, arr))
```
