
from collections import defaultdict

def dfs(node, visited, graph):
visited.add(node)
for neighbour in graph[node]:
if neighbour not in visited:
dfs(neighbour, visited, graph)

def count_round_trips(n, m, roads):
graph = defaultdict(list)
for x, y in roads:
graph[x].append(y)
visited = set()
count = 0
for i in range(n):
if i not in visited:
dfs(i, visited, graph)
count += 1
return count

def main():
n, m = map(int, input().split())
roads = []
for _ in range(m):
x, y = map(int, input().split())
roads.append((x, y))
print(count_round_trips(n, m, roads))

if __name__ == "__main__":
main()

