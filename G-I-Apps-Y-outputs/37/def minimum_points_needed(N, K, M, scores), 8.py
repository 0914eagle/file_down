
def minimum_points_needed(N, K, M, scores):
    current_total = sum(scores)
    points_needed = max(0, N*M - current_total)
    
    if points_needed <= K:
        return points_needed
    else:
        return -1

# Read input
N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

# Call the function and print the result
print(minimum_points_needed(N, K, M, scores))
```
