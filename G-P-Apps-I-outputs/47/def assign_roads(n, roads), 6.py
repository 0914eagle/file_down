
def assign_roads(n, roads):
    city_roads = {}
    for i, (a, b) in enumerate(roads):
        city_roads[i+1] = (a, b)

    for city, (a, b) in city_roads.items():
        print(f"{a} {b}")

# Input parsing
n = int(input())
roads = [list(map(int, input().split())) for _ in range(n)]

# Call the function
assign_roads(n, roads)
```
