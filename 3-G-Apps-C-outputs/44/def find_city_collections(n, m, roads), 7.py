
def find_city_collections(n, m, roads):
    graph = {i: set() for i in range(1, n+1)}
    for road in roads:
        x, y = road
        graph[x].add(y)
        graph[y].add(x)
    
    if len(graph[1]) + len(graph[2]) < n - 2:
        print("impossible")
        return
    
    arya_cities = [1]
    sansa_cities = [2]
    
    for city in range(3, n+1):
        if city in graph[1] and city not in graph[2]:
            arya_cities.append(city)
        elif city in graph[2] and city not in graph[1]:
            sansa_cities.append(city)
    
    print(" ".join(map(str, arya_cities)))
    print(" ".join(map(str, sansa_cities))

# Input
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

# Call the function
find_city_collections(n, m, roads)
