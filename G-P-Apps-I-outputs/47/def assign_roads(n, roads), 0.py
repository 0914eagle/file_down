
def assign_roads(n, roads):
    cities = {}
    result = []
    for road in roads:
        city1, city2 = road
        if city1 not in cities:
            cities[city1] = city2
            result.append((city1, city2))
        elif city2 not in cities:
            cities[city2] = city1
            result.append((city2, city1))
    
    for city in range(1, n + 1):
        if city not in cities:
            result.append((city, 1))
    
    return result

n = int(input())
roads = [list(map(int, input().split())) for _ in range(n)]
output = assign_roads(n, roads)
for road in output:
    print(road[0], road[1])
```
