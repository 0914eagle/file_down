
def min_total_distance(N, K, balls):
    min_distance = 0
    for ball in balls:
        min_distance += min(ball * 2, (K - ball) * 2)
    return min_distance

# Reading input
N = int(input())
K = int(input())
balls = list(map(int, input().split()))

# Calling the function and printing the result
print(min_total_distance(N, K, balls))
