
def min_points_for_goal(N, K, M, A):
    current_total = sum(A)
    remaining_subjects = N - len(A)
    min_points_needed = max(0, N * M - current_total)
    
    if min_points_needed > K:
        return -1
    else:
        return min_points_needed

# Read input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Output result
print(min_points_for_goal(N, K, M, A))
```
