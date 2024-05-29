
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_divisor(arr):
    result = []
    for i in range(len(arr)):
        max_score = 0
        for j in range(i, len(arr)):
            gcd = arr[i]
            for k in range(i, j+1):
                gcd = math.gcd(gcd, arr[k])
            
            if is_prime(gcd):
                max_score = max(max_score, gcd)
        result.append(max_score)
    return result

def max_score_partition(n, k, arr):
    max_scores = largest_prime_divisor(arr)
    dp = [[float('inf')] * (k+1) for _ in range(n+1)]
    dp[0][0] = 0
    
    for i in range(1, n+1):
        for j in range(1, min(k, i)+1):
            for x in range(i):
                dp[i][j] = min(dp[i][j], max(dp[x][j-1], max_scores[x]))
    
    return dp[n][k]

# Read input values
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function and print the result
print(max_score_partition(n, k, arr))
```
