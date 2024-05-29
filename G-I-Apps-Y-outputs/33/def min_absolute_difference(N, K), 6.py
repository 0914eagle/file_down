
def min_absolute_difference(N, K):
    return (N % K) if N % K <= K // 2 else K - (N % K)

# Taking input
N, K = map(int, input().split())

# Calling the function and printing the result
print(min_absolute_difference(N, K))
```
