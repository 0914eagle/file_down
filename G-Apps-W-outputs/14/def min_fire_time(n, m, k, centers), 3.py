
def min_fire_time(n, m, k, centers):
    def distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    max_distance = 0
    for i in range(k):
        for j in range(i+1, k):
            dist = distance(centers[i][0], centers[i][1], centers[j][0], centers[j][1])
            max_distance = max(max_distance, (dist + 1) // 2)
    
    max_distance = max(max_distance, max(centers[0][0]-1, n-centers[0][0], centers[0][1]-1, m-centers[0][1]))
    
    print(max_distance)

# Input
n, m, k = map(int, input().split())
centers = [tuple(map(int, input().split())) for _ in range(k)]

min_fire_time(n, m, k, centers)
