
def assign_roads(n, roads):
    assigned_roads = []
    cities = set(range(1, n + 1))

    for road in roads:
        a, b = road
        assigned_roads.append((a, b))

    for city in cities:
        if city not in [road[0] for road in assigned_roads]:
            assigned_roads.append((city, list(cities - set([road[0] for road in assigned_roads]))[0])

    for road in assigned_roads:
        print(road[0], road[1])

# Sample Input
n = 4
roads = [(1, 2), (2, 3), (3, 1), (4, 1)]

assign_roads(n, roads)
```
