
from sys import stdin
from collections import defaultdict

def main():
    n, m, k = map(int, stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        x, y, w = map(int, stdin.readline().split())
        graph[x].append((y, w))
        graph[y].append((x, w))
    routes = [tuple(map(int, stdin.readline().split())) for _ in range(k)]
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i in range(n):
        for j in graph[i + 1]:
            dist[i][j[0] - 1] = j[1]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    min_cost = float('inf')
    for i in range(n):
        for j in range(n):
            cost = 0
            for a, b in routes:
                cost += dist[a - 1][b - 1]
            min_cost = min(min_cost, cost)
            dist[i][j] = 0
    print(min_cost)

main()

