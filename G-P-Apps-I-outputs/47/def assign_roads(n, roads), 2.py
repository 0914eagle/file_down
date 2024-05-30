
def assign_roads(n, roads):
    assigned_roads = {}
    cities = set(range(1, n+1))

    for road in roads:
        city_a, city_b = road
        if city_a in cities and city_b in cities:
            assigned_roads[city_a] = city_b
            cities.remove(city_a)
        elif city_a in cities:
            assigned_roads[city_a] = city_b
        elif city_b in cities:
            assigned_roads[city_b] = city_a

    for city in cities:
        assigned_roads[city] = city

    for city, road in assigned_roads.items():
        print(city, road)

n = 4
roads = [[1, 2], [2, 3], [3, 1], [4, 1]]
assign_roads(n, roads)
```
