
def min_time_to_light_up(n, m, k, centers):
    max_dist = 0
    for i in range(k):
        for j in range(i + 1, k):
            dist = max(abs(centers[i][0] - centers[j][0]), abs(centers[i][1] - centers[j][1]))
            max_dist = max(max_dist, dist // 2)
    
    max_dist = min(max_dist, max(n - centers[0][0], centers[0][0] - 1, m - centers[0][1], centers[0][1] - 1))
    
    return max_dist

# Reading input
n, m, k = map(int, input().split())
centers = []
for _ in range(k):
    x, y = map(int, input().split())
    centers.append((x, y))

# Calculating and printing output
print(min_time_to_light_up(n, m, k, centers))
