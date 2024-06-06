
import sys
import heapq

n = int(sys.stdin.readline().strip())
costs = list(map(int, sys.stdin.readline().strip().split()))

def graph_init():
    G = {}
    for i in range(n):
        G[i+1] = {}
    return G

G = graph_init()

for i in range(n):
    C = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(1, C[0]+1):
        G[i+1][C[j]] = costs[C[j]-1]

q = [(0, 1)]
visited = set()
while q:
    cost, node = heapq.heappop(q)
    if node not in visited:
        visited.add(node)
        for neighbor, w in G[node].items():
            if neighbor not in visited:
                heapq.heappush(q, (cost+w, neighbor))
print(cost)
