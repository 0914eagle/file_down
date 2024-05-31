
def min_total_distance(N, K, x):
    min_distance = float('inf')
    for i in range(N):
        distance = min(x[i], K - x[i]) * 2 + K
        min_distance = min(min_distance, distance)
    return min_distance

# Reading inputs from Standard Input
N = int(input())
K = int(input())
x = list(map(int, input().split()))

# Calculating and printing the minimum possible total distance covered by robots
print(min_total_distance(N, K, x))
