
def assign_roads(n, roads):
    city_roads = {}
    for i in range(n):
        city_roads[i+1] = []

    for road in roads:
        city, other_city = road
        city_roads[city].append(other_city)

    result = []
    for city, connected_cities in city_roads.items():
        for connected_city in connected_cities:
            result.append((city, connected_city))

    for road in result:
        print(f"{road[0]} {road[1]}")

n = 4
roads = [(1, 2), (2, 3), (3, 1), (4, 1)]
assign_roads(n, roads)
```
