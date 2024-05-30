
def assign_roads(n, roads):
    assignment = {}
    for i in range(1, n+1):
        assignment[i] = None

    for road in roads:
        a, b = road
        if assignment[a] is None:
            assignment[a] = b
        else:
            assignment[b] = a

    for city, road_built in assignment.items():
        print(city, road_built)

# Sample Input
n = 4
roads = [
    [1, 2],
    [2, 3],
    [3, 1],
    [4, 1]
]

assign_roads(n, roads)
```
