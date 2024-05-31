
def min_total_distance(N, K, x):
    min_distance = float('inf')
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            distance = abs(x[i-1] - 0) + abs(x[j-1] - K)  # Distance of type-A robot to ball and back + Distance of type-B robot to ball and back
            min_distance = min(min_distance, distance)
    
    return min_distance

# Input
N = int(input())
K = int(input())
x = list(map(int, input().split()))

# Output
print(min_total_distance(N, K, x))
