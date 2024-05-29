
def minimum_points_required(N, K, M, scores):
    total_points = sum(scores)
    min_points_required = max(0, N * M - total_points)
    return min_points_required if min_points_required <= K else -1

# Input processing
N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

# Call the function with the input values
result = minimum_points_required(N, K, M, scores)
print(result)
```
