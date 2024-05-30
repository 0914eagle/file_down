
def minimum_points_needed(N, K, M, scores):
    total_points = sum(scores)
    min_points = max(0, N*M - total_points)
    return min_points if min_points <= K else -1

# Reading input
N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

# Output
print(minimum_points_needed(N, K, M, scores))
```
