
def calculate_points_needed(N, K, M, scores):
    total_points = sum(scores)
    min_points_needed = max(0, N * M - total_points)
    if min_points_needed <= K:
        return min_points_needed
    else:
        return -1

# Input processing
input_data = input().split()
N = int(input_data[0])
K = int(input_data[1])
M = int(input_data[2])
scores = list(map(int, input().split()))

result = calculate_points_needed(N, K, M, scores)
print(result)
```
