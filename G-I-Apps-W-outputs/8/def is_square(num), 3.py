
def is_square(num):
    return int(num ** 0.5) ** 2 == num

def shortest_perfect_square_subsequence_length(n, arr):
    dp = [-1] * (1 << 8)
    dp[0] = 0
    for x in arr:
        mask = 0
        for i in range(2, 8):
            cnt = 0
            while x % i == 0:
                x //= i
                cnt += 1
            if cnt & 1:
                mask |= 1 << (i-2)
        
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] != -1:
                dp[i | mask] = max(dp[i | mask], dp[i] + 1)
    
    ans = float('inf')
    for i in range(1, 1 << 8):
        if is_square(i):
            ans = min(ans, dp[i])
    
    if ans == float('inf'):
        return -1
    return ans

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(shortest_perfect_square_subsequence_length(n, arr))
```
