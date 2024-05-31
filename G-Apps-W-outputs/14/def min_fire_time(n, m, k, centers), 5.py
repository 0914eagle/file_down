
import math

def min_fire_time(n, m, k, centers):
    max_dist = 0
    
    for i in range(k):
        for j in range(i+1, k):
            dist = max(abs(centers[i][0] - centers[j][0]), abs(centers[i][1] - centers[j][1]))
            max_dist = max(max_dist, dist)
    
    min_time = math.ceil(max_dist / 2)
    
    for i in range(k):
        min_time = max(min_time, max(abs(centers[i][0] - 1), abs(centers[i][1] - 1), abs(centers[i][0] - n), abs(centers[i][1] - m)))
    
    return min_time

# Input
n, m, k = map(int, input().split())
centers = [tuple(map(int, input().split())) for _ in range(k)]

# Output
print(min_fire_time(n, m, k, centers))
