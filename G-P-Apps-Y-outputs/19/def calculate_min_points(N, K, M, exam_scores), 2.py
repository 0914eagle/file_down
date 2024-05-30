
def calculate_min_points(N, K, M, exam_scores):
    total_points = sum(exam_scores)
    remaining_subjects = N - 1
    min_points_needed = max(0, N * M - total_points)
    
    if min_points_needed <= K:
        return min_points_needed
    else:
        return -1

# Read input
N, K, M = map(int, input().split())
exam_scores = list(map(int, input().split()))

# Output result
print(calculate_min_points(N, K, M, exam_scores))
```
