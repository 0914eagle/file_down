
def min_time_to_lighten_city(n, m, k, centers):
    max_distance = 0
    for i in range(k):
        for j in range(i + 1, k):
            distance = max(abs(centers[i][0] - centers[j][0]), abs(centers[i][1] - centers[j][1]))
            max_distance = max(max_distance, distance)
    
    min_time = max_distance // 2 + max_distance % 2
    return min_time

# Input
n, m, k = map(int, input().split())
centers = []
for _ in range(k):
    x, y = map(int, input().split())
    centers.append((x, y))

# Output
print(min_time_to_lighten_city(n, m, k, centers))
