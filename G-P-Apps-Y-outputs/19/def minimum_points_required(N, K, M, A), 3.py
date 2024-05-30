
def minimum_points_required(N, K, M, A):
    total_points = sum(A)
    min_points_needed = max(0, N*M - total_points)
    if min_points_needed > K:
        return -1
    return min_points_needed

# Read input from Standard Input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
print(minimum_points_required(N, K, M, A))
```
