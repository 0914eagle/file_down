
def min_distance(N, K, balls):
    distance_A = sum(min(ball, K - ball) * 2 for ball in balls)
    distance_B = sum(min(K - ball, ball) * 2 for ball in balls)
    
    return min(distance_A, distance_B)

# Reading input values
N = int(input())
K = int(input())
balls = list(map(int, input().split()))

# Calculate and print the minimum total distance covered by robots
print(min_distance(N, K, balls))
