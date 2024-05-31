
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def find_min_aqueduct_length(n, s, t, q, hills, springs, towns):
    graph = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0
    
    for i in range(n):
        for j in range(n):
            if i != j:
                x1, y1, h1 = hills[i]
                x2, y2, h2 = hills[j]
                distance = calculate_distance(x1, y1, x2, y2)
                if distance <= q:
                    graph[i][j] = distance
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    total_length = 0
    for town in towns:
        spring_distances = [graph[spring-1][town-1] for spring in springs]
        min_spring_distance = min(spring_distances)
        if min_spring_distance == float('inf'):
            return "IMPOSSIBLE"
        total_length += min_spring_distance
    
    return round(total_length, 6)

# Input parsing
n, s, t, q = map(int, input().split())
hills = []
for _ in range(n):
    hills.append(list(map(int, input().split())))

springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Call the function and print the result
result = find_min_aqueduct_length(n, s, t, q, hills, springs, towns)
print(result)
