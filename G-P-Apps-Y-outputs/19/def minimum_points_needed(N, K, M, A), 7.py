
def minimum_points_needed(N, K, M, A):
    total_points = sum(A)
    remaining_subjects = N - 1
    min_points_needed = max(0, N * M - total_points)
    
    if min_points_needed <= K:
        return min_points_needed
    else:
        return -1

# Input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Output
print(minimum_points_needed(N, K, M, A))
```
