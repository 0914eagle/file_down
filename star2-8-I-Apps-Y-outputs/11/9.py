
from collections import defaultdict

def solve(gangs):
  graph = defaultdict(list)
  for i in range(1, len(gangs)):
    graph[gangs[i-1]].append(gangs[i])
    graph[gangs[i]].append(gangs[i-1])
  if not check_connection(graph, gangs[0]):
    return "NO"
  if not check_valid_roads(graph):
    return "NO"
  res = []
  for k, v in graph.items():
    for c in v:
      if k < c:
        res.append(f"{k} {c}")
  return "YES\n" + "\n".join(res)


def check_connection(graph, start):
  visited = {start}
  queue = [start]
  while queue:
    v = queue.pop(0)
    for c in graph[v]:
      if c not in visited:
        visited.add(c)
        queue.append(c)
  return len(visited) == len(graph)


def check_valid_roads(graph):
  for k, v in graph.items():
    for c in v:
      if k > c and graph[c].count(k) == 0:
        return False
  return True


t = int(input())
for _ in range(t):
  n = int(input())
  gangs = list(map(int, input().split()))
  print(solve(gangs))

