
def minimum_points_needed(N, K, M, A):
    current_total = sum(A)
    remaining_subjects = N - 1
    min_points_needed = max(0, N*M - current_total)
    return min_points_needed if min_points_needed <= K else -1

# Take input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
result = minimum_points_needed(N, K, M, A)
print(result)
```
