
def min_total_distance(N, K, x):
    total_distance = 0

    for xi in x:
        distance_to_ball = min(xi, K-xi)
        total_distance += 2 * distance_to_ball

    return total_distance

# Read input
N = int(input())
K = int(input())
x = list(map(int, input().split()))

# Calculate and print the minimum total distance
print(min_total_distance(N, K, x))
