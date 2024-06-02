
import math

def distance(tower1, tower2):
    return math.sqrt((tower1[0] - tower2[0])**2 + (tower1[1] - tower2[1])**2)

def can_reach(tower1, tower2):
    return distance(tower1, tower2) <= 2

def dfs(towers, visited, current):
    visited[current] = True
    for i in range(len(towers)):
        if not visited[i] and can_reach(towers[current], towers[i]):
            dfs(towers, visited, i)

def max_connected_towers(n, towers):
    max_towers = 0
    for i in range(n):
        visited = [False] * n
        dfs(towers, visited, i)
        max_towers = max(max_towers, sum(visited))
    return max_towers

# Read input
n = int(input())
towers = []
for _ in range(n):
    x, y = map(float, input().split())
    towers.append((x, y))

# Add one more tower at a random location
towers.append((100001.0, 100001.0))

# Calculate the maximum number of connected towers
result = max_connected_towers(n+1, towers)
print(result)
