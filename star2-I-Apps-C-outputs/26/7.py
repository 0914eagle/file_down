
from collections import defaultdict

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start in visited:
        return False
    visited.add(start)
    for next in graph[start]:
        if next not in visited:
            if dfs(graph, next, visited):
                return True
    return True

def count_round_trips(towns, roads):
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
    count = 0
    for town in towns:
        if dfs(graph, town):
            count += 1
    return count

def find_max_new_roads(towns, roads):
    return 0

towns = [0, 1]
roads = [[0, 1]]
max_new_roads = find_max_new_roads(towns, roads)
print(f"Maximum number of new roads: {max_new_roads}")

