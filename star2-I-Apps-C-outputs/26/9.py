
from collections import defaultdict

def find_round_trips(towns, roads):
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
    visited = set()
    round_trips = set()

    def dfs(town, path):
        if town in visited:
            return
        visited.add(town)
        path.append(town)
        for neighbor in graph[town]:
            if neighbor == path[0]:
                round_trips.add(tuple(path))
            else:
                dfs(neighbor, path)
        path.pop()

    for town in towns:
        dfs(town, [])
    return round_trips

def count_new_round_trips(towns, roads, new_road):
    round_trips = find_round_trips(towns, roads)
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
    graph[new_road[0]].append(new_road[1])
    visited = set()
    new_round_trips = set()

    def dfs(town, path):
        if town in visited:
            return
        visited.add(town)
        path.append(town)
        for neighbor in graph[town]:
            if neighbor == path[0]:
                new_round_trips.add(tuple(path))
            else:
                dfs(neighbor, path)
        path.pop()

    for town in towns:
        dfs(town, [])
    return len(new_round_trips) - len(round_trips)
towns = [0, 1, 2, 3]
roads = [(0, 1), (1, 2), (2, 3), (3, 0)]
new_road = (0, 2)
count = count_new_round_trips(towns, roads, new_road)
print(f"Number of new round trips: {count}")

