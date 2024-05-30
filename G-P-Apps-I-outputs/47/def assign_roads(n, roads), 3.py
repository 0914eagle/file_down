
def assign_roads(n, roads):
    assigned_roads = {}
    for i, road in enumerate(roads):
        city = i + 1
        assigned_roads[city] = road[0]
    
    for city, road in assigned_roads.items():
        print(city, road)

n = 4
roads = [(1, 2), (2, 3), (3, 1), (4, 1)]
assign_roads(n, roads)
```
