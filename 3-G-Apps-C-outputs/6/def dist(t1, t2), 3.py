
import math

def dist(t1, t2):
    return math.sqrt((t1[0] - t2[0])**2 + (t1[1] - t2[1])**2)

def dfs(towers, visited, curr):
    visited[curr] = True
    for i in range(len(towers)):
        if not visited[i] and dist(towers[curr], towers[i]) <= 2:
            dfs(towers, visited, i)

def max_connected_towers(n, towers):
    towers.append((0, 0))  # Add a virtual tower at (0, 0)
    visited = [False] * (n + 1)
    connected_regions = 0

    for i in range(n + 1):
        if not visited[i]:
            dfs(towers, visited, i)
            connected_regions += 1

    return connected_regions

# Read input
n = int(input())
towers = []
for _ in range(n):
    x, y = map(float, input().split())
    towers.append((x, y))

# Calculate and output the result
print(max_connected_towers(n, towers))
