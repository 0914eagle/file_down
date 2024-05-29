
def min_points_needed(N, K, M, A):
    total_points = sum(A)
    min_points = max(M * N - total_points, 0)
    return min_points if min_points <= K else -1

# Input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Output
print(min_points_needed(N, K, M, A))
```
