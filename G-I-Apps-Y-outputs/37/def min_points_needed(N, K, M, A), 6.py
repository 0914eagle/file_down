
def min_points_needed(N, K, M, A):
    total_points = sum(A)
    min_points = max(0, N*M - total_points)
    
    if min_points > K:
        return -1
    else:
        return min_points

# Input processing
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Display output
print(min_points_needed(N, K, M, A))
```
