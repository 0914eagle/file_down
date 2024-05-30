
def minimum_points_needed(N, K, M, A):
    total_points = sum(A)
    min_points_needed = max(0, N * M - total_points)
    return min_points_needed if min_points_needed <= K else -1

# Read input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
print(minimum_points_needed(N, K, M, A))
```
