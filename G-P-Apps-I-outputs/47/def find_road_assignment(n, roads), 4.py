
def find_road_assignment(n, roads):
    road_assignment = {}
    for i, (a, b) in enumerate(roads, start=1):
        road_assignment[b] = a
    for city, road in road_assignment.items():
        print(f"{city} {road}")

n = 4
roads = [(1, 2), (2, 3), (3, 1), (4, 1)]
find_road_assignment(n, roads)
```
