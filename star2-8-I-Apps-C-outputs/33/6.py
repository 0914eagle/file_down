
from sys import stdin
from collections import defaultdict

class Graph:
def __init__(self, vertices):
self.graph = defaultdict(list)
self.V = vertices

def addEdge(self, u, v):
self.graph[u].append(v)

def dfs(self, v, visited, path):
visited[v] = True
path.append(v)
for i in self.graph[v]:
if not visited[i]:
self.dfs(i, visited, path)
return path

def get_chance_of_success(self):
path = self.dfs(0, [False] * (self.V), [])
total_rooms = len(path)
captain_walk_rooms = list(map(int, stdin.readline().split()))
rooms_visited_by_captain = defaultdict(int)
for room in captain_walk_rooms:
rooms_visited_by_captain[room] += 1
sentry_rooms = []
sentry_chance_of_success = 1
for i in range(self.V):
if path.count(i) > rooms_visited_by_captain[i]:
sentry_rooms.append(i)
sentry_chance_of_success *= (1/total_rooms)
chance_of_success = 1 - sentry_chance_of_success
return chance_of_success


if __name__ == '__main__':
N = int(stdin.readline())
L = int(stdin.readline())
g = Graph(N)
for _ in range(N):
u, *neighbors = map(int, stdin.readline().split())
for v in neighbors:
g.addEdge(u, v)
print(g.get_chance_of_success())

