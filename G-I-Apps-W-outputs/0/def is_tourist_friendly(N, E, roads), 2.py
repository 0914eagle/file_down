
def is_tourist_friendly(N, E, roads):
    adj_list = {i: [] for i in range(1, N + 1)}

    for a, b in roads:
        adj_list[a].append(b)

    out_deg = [0] * (N + 1)
    in_deg = [0] * (N + 1)

    for a, b in roads:
        out_deg[a] += 1
        in_deg[b] += 1

    start_city = None
    end_city = None

    for i in range(1, N + 1):
        if out_deg[i] != in_deg[i]:
            if out_deg[i] - in_deg[i] == 1:
                if end_city is not None:
                    return ("NO", [])
                end_city = i
            elif in_deg[i] - out_deg[i] == 1:
                if start_city is not None:
                    return ("NO", [])
                start_city = i
            else:
                return ("NO", [])

    if start_city is None and end_city is None:
        start_city = roads[0][0]

    stack = []
    circuit = []

    def dfs(v):
        while adj_list[v]:
            u = adj_list[v][-1]
            adj_list[v].pop()
            dfs(u)
        circuit.append(v)

    dfs(start_city)

    circuit = circuit[::-1]

    if circuit[0] != start_city or circuit[-1] != end_city:
        return ("NO", [])

    for i in range(len(circuit) - 1):
        if (circuit[i], circuit[i + 1]) not in roads:
            roads.append((circuit[i], circuit[i + 1]))

    return ("YES", roads)

# Input parsing
N, E = map(int, input().split())
roads = []
for _ in range(E):
    a, b = map(int, input().split())
    roads.append((a, b))

result, new_roads = is_tourist_friendly(N, E, roads)
print(result)
if result == "YES":
    for road in new_roads:
        print(road[0], road[1])
```
