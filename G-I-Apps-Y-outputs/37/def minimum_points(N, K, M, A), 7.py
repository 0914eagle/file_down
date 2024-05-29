
def minimum_points(N, K, M, A):
    current_total = sum(A)
    min_points_needed = max(0, N * M - current_total)
    return min_points_needed if min_points_needed <= K else -1

# Read input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
result = minimum_points(N, K, M, A)
print(result)
```
