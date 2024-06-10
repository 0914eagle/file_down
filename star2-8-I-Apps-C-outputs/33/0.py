
from collections import defaultdict
import math


def solve(nodes, rooms, walk, graph):
    n = len(nodes)
    sentry_pos = -1
    captain_pos = -1
    vis = [False] * n
    for i, node in enumerate(nodes):
        if node == 0:
            sentry_pos = i
            vis[i] = True
            break
    for i, room in enumerate(walk):
        if room == sentry_pos:
            captain_pos = i
            break
    def bfs(node):
        vis = [False] * n
        queue = [node]
        vis[node] = True
        while queue:
            curr = queue.pop(0)
            for neighbour in graph[curr]:
                if not vis[neighbour]:
                    vis[neighbour] = True
                    queue.append(neighbour)
        return vis
    
    graph = defaultdict(list)
    for i in range(n):
        for j in nodes[i]:
            graph[i].append(j)
    sentry_reachable = bfs(sentry_pos)
    captain_reachable = bfs(captain_pos)
    for i in range(n):
        if sentry_reachable[i] and captain_reachable[i]:
            return 0
    
    sentry_prob = 1 / sum(sentry_reachable)
    captain_prob = 1 / sum(captain_reachable)
    if captain_pos == 0 or captain_pos == len(walk) - 1:
        return sentry_prob * captain_prob
    return math.exp(-sentry_prob * captain_prob * len(walk))

n = int(input())
l = int(input())
walk = [int(x) for x in input().split()]
nodes = []
for _ in range(n):
    nodes.append([int(x) for x in input().split()])
print(solve(nodes, walk, l, n))

