
import math

def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num

def shortest_perfect_square_subsequence(n, arr):
    dp = [set() for _ in range(n)]
    
    for i in range(n):
        dp[i].add(arr[i])
        for j in range(i):
            temp = dp[j].copy()
            for num in dp[j]:
                if not is_perfect_square(num * arr[i]):
                    temp.add(num * arr[i])
            dp[i] |= temp
    
    result = float('inf')
    for s in dp:
        for num in s:
            if is_perfect_square(num):
                result = min(result, len(s))
                
    return result if result != float('inf') else -1

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(shortest_perfect_square_subsequence(n, arr))
```
