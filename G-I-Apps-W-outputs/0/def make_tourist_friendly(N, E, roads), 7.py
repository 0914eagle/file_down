
def make_tourist_friendly(N, E, roads):
    adj_list = {}
    for a, b in roads:
        if a not in adj_list:
            adj_list[a] = []
        adj_list[a].append(b)

    indegrees = [0] * (N + 1)
    outdegrees = [0] * (N + 1)
    for a, b in roads:
        outdegrees[a] += 1
        indegrees[b] += 1

    start_city = None
    end_city = None
    for i in range(1, N+1):
        if indegrees[i] == outdegrees[i]:
            continue
        if indegrees[i] == outdegrees[i] + 1:
            if end_city is not None:
                return "NO"
            end_city = i
        elif indegrees[i] + 1 == outdegrees[i]:
            if start_city is not None:
                return "NO"
            start_city = i
        else:
            return "NO"

    if start_city is None and end_city is None:
        start_city = roads[0][0]
        end_city = roads[0][1]

    if start_city is None or end_city is None:
        return "NO"

    path = [start_city]
    
    def dfs(city):
        while city in adj_list and adj_list[city]:
            next_city = adj_list[city].pop()
            dfs(next_city)
        path.append(city)

    dfs(start_city)

    if len(path) - 1 != E:
        return "NO"
    path.reverse()

    result = "YES\n"
    for i in range(len(path) - 1):
        result += f"{path[i]} {path[i+1]}\n"

    return result

# Example usage
N, E = 3, 3
roads = [(1, 2), (2, 3), (3, 1)]
print(make_tourist_friendly(N, E, roads))

N, E = 3, 2
roads = [(1, 2), (2, 3)]
print(make_tourist_friendly(N, E, roads))

N, E = 5, 6
roads = [(1, 2), (2, 3), (3, 4), (2, 4), (2, 5), (1, 5)]
print(make_tourist_friendly(N, E, roads))
```
