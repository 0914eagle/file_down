
def minimum_points_needed(N, K, M, scores):
    total_score = sum(scores)
    remaining_subjects = N - 1
    remaining_score = max(0, M * N - total_score)
    
    if remaining_score <= K:
        return remaining_score
    else:
        return -1

# Input parsing
N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

# Calling the function with input values
result = minimum_points_needed(N, K, M, scores)
print(result)
```
