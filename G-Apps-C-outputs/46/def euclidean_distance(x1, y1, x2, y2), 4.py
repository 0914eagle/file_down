
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_min_aqueduct_length(n, s, t, q, hills, springs, towns):
    min_aqueduct_length = float('inf')
    
    for spring_hill in springs:
        for town_hill in towns:
            if spring_hill != town_hill:
                distances = []
                for i in range(n):
                    x1, y1, h1 = hills[spring_hill - 1]
                    x2, y2, h2 = hills[i]
                    distance1 = euclidean_distance(x1, y1, x2, y2)
                    
                    x3, y3, h3 = hills[town_hill - 1]
                    x4, y4, h4 = hills[i]
                    distance2 = euclidean_distance(x3, y3, x4, y4)
                    
                    if h1 >= h2 and h3 >= h4:
                        distances.append(distance1 + distance2)
                
                if distances:
                    min_aqueduct_length = min(min_aqueduct_length, max(distances))
    
    if min_aqueduct_length <= q:
        return min_aqueduct_length
    else:
        return "IMPOSSIBLE"

# Input parsing
n, s, t, q = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(n)]
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Call the function with the input values
result = find_min_aqueduct_length(n, s, t, q, hills, springs, towns)
print(result)
