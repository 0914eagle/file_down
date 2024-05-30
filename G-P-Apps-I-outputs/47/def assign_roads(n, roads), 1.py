
def assign_roads(n, roads):
    road_assignments = []
    cities = list(range(1, n + 1))

    for city, (a, b) in zip(cities, roads):
        road_assignments.append((city, a))

    return road_assignments

# Input parsing
n = int(input())
roads = []
for _ in range(n):
    a, b = map(int, input().split())
    roads.append((a, b))

# Find road assignments
assigned_roads = assign_roads(n, roads)

# Output road assignments
for city, road in assigned_roads:
    print(f"{city} {road}")
```
