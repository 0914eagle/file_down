
def minimum_points_needed(N, K, M, scores):
    total_points = sum(scores)
    remaining_exams = N - 1
    required_points = max(0, N * M - total_points)
    
    if required_points <= K:
        return required_points
    else:
        return -1

# Input processing
N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

result = minimum_points_needed(N, K, M, scores)
print(result)
```
