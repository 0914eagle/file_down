
def assign_roads(n, roads):
    city_to_road = {}
    for i, (a, b) in enumerate(roads):
        city_to_road[a] = i + 1
    for city, road in city_to_road.items():
        print(city, road)

n = 4
roads = [(1, 2), (2, 3), (3, 1), (4, 1)]
assign_roads(n, roads)
```
