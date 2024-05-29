
def minimum_points_needed(N, K, M, scores):
    current_sum = sum(scores)
    remaining_subjects = N - len(scores)
    min_points = max(0, N * M - current_sum)
    return min_points if min_points <= K else -1

# Input parsing
N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

# Call the function
result = minimum_points_needed(N, K, M, scores)
print(result)
```
