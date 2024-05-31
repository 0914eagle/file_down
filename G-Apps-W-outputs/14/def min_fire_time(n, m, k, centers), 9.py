
def min_fire_time(n, m, k, centers):
    max_dist = 0
    for i in range(k):
        for j in range(i+1, k):
            dist = max(abs(centers[i][0] - centers[j][0]), abs(centers[i][1] - centers[j][1]))
            max_dist = max(max_dist, dist)
    
    max_dist = max(max_dist, max(centers[-1][0]-1, n - centers[-1][0], centers[-1][1]-1, m - centers[-1][1]))
    
    print(max_dist)

# Input
n, m, k = map(int, input().split())
centers = [tuple(map(int, input().split())) for _ in range(k)]

# Call the function
min_fire_time(n, m, k, centers)
