
from collections import defaultdict

def dfs(node, parent, adj_list, universities, distances):
    total_distance = 0
    for child in adj_list[node]:
        if child != parent:
            child_distance = dfs(child, node, adj_list, universities, distances)
            distances[node][child] = distances[child][node] = child_distance
            total_distance += child_distance
    if node in universities:
        return 0
    return 1 + total_distance

def find_max_distance(n, k, universities, roads):
    adj_list = defaultdict(list)
    for x, y in roads:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    distances = defaultdict(dict)
    dfs(universities[0], -1, adj_list, universities, distances)
    
    max_distance = 0
    for u in universities:
        for v in universities:
            if u != v:
                max_distance = max(max_distance, distances[u][v])
    
    return max_distance

# Input parsing
n, k = map(int, input().split())
universities = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n-1)]

# Call the function and print the output
print(find_max_distance(n, k, universities, roads))
