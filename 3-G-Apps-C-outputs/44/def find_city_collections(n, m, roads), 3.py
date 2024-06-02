
def find_city_collections(n, m, roads):
    graph = {i: set() for i in range(1, n+1)}
    for road in roads:
        x, y = road
        graph[x].add(y)
        graph[y].add(x)

    arya_cities = set()
    sansa_cities = set()

    for city in graph[1]:
        if city != 2:
            arya_cities.add(city)

    for city in graph[2]:
        if city != 1:
            sansa_cities.add(city)

    remaining_cities = set(range(1, n+1)) - arya_cities - sansa_cities

    for city in remaining_cities:
        if city != 1 and city != 2:
            arya_cities.add(city)

    if len(remaining_cities) == 0:
        print("impossible")
    else:
        print(" ".join(map(str, [1] + list(arya_cities)))
        print(" ".join(map(str, [2] + list(sansa_cities)))

# Input parsing
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

find_city_collections(n, m, roads)
