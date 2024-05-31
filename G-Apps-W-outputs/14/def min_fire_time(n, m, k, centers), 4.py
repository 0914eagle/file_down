
def min_fire_time(n, m, k, centers):
    max_dist = 0
    for center in centers:
        for i in range(1, n+1):
            for j in range(1, m+1):
                dist = abs(center[0] - i) + abs(center[1] - j)
                max_dist = max(max_dist, dist)
    
    return max_dist

n, m, k = map(int, input().split())
centers = []
for _ in range(k):
    x, y = map(int, input().split())
    centers.append((x, y))

print(min_fire_time(n, m, k, centers))
