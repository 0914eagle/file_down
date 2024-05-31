
def min_time_to_lighten(n, m, k, centers):
    max_dist = 0
    for i in range(k):
        for j in range(i+1, k):
            dist = max(abs(centers[i][0] - centers[j][0]), abs(centers[i][1] - centers[j][1]))
            max_dist = max(max_dist, dist)
    
    max_dist = max(max_dist, max(centers[0][0] - 1, n - centers[k-1][0], centers[0][1] - 1, m - centers[k-1][1]))
    
    return max_dist

# Input parsing
n, m, k = map(int, input().split())
centers = []
for _ in range(k):
    x, y = map(int, input().split())
    centers.append((x, y))

# Call the function and output the result
result = min_time_to_lighten(n, m, k, centers)
print(result)
