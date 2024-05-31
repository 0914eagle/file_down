
import math

def distance(hill1, hill2):
    x1, y1, h1 = hill1
    x2, y2, h2 = hill2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (h1 - h2) ** 2)

def find_min_aqueduct_length(n, s, t, q, hills, springs, towns):
    distances = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        distances[i][i] = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(hills[i], hills[j])
            if dist <= q:
                distances[i][j] = distances[j][i] = dist
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    total_length = 0
    for town in towns:
        min_length = float('inf')
        for spring in springs:
            min_length = min(min_length, distances[spring-1][town-1])
        if min_length == float('inf'):
            return "IMPOSSIBLE"
        total_length += min_length
    
    return round(total_length, 6)

# Input reading
n, s, t, q = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(n)]
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Output
print(find_min_aqueduct_length(n, s, t, q, hills, springs, towns))
