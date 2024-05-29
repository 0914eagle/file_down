
def minimum_points_needed(N, K, M, scores):
    total_points = sum(scores)
    remaining_subjects = N - 1
    remaining_points = max(0, M * N - total_points)
    
    if remaining_points <= K:
        return remaining_points
    else:
        return -1

# Input
N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

# Output
print(minimum_points_needed(N, K, M, scores))
