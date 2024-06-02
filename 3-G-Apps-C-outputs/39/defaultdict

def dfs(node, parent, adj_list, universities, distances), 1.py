
from collections import defaultdict

def dfs(node, parent, adj_list, universities, distances):
    total_dist = 0
    for child in adj_list[node]:
        if child != parent:
            child_dist = dfs(child, node, adj_list, universities, distances)
            total_dist += child_dist
    if node in universities:
        distances[node] = total_dist
        return 0
    return total_dist + 1

def find_max_distance(n, k, universities, roads):
    adj_list = defaultdict(list)
    for x, y in roads:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    distances = {}
    dfs(universities[0], -1, adj_list, set(universities), distances)
    
    max_distances = sorted(distances.values(), reverse=True)[:k]
    return sum(max_distances)

# Input parsing
n, k = map(int, input().split())
universities = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n-1)]

# Output
print(find_max_distance(n, k, universities, roads))
