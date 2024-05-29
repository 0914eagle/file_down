
def minimum_points_needed(N, K, M, scores):
    total_points = sum(scores)
    remaining_subjects = N - 1
    min_points = max(0, N * M - total_points)
    
    if min_points > K:
        return -1
    else:
        return min_points

# Read input from Standard Input
N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

# Call the function and print the result
print(minimum_points_needed(N, K, M, scores))
``` 
