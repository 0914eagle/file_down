
def min_total_distance(N, K, x):
    min_dist = 0
    for xi in x:
        dist_A = abs(xi) * 2
        dist_B = abs(K - xi) * 2
        min_dist += min(dist_A, dist_B)
    return min_dist

# Read input
N = int(input())
K = int(input())
x = list(map(int, input().split()))

# Calculate and print the minimum possible total distance covered by robots
print(min_total_distance(N, K, x))
