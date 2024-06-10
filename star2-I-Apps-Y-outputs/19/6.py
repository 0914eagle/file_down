
import sys
input = sys.stdin.readline

def main():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        x -= 1
        y -= 1
        adj[x].append((y, w))
        adj[y].append((x, w))
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i in range(n):
        for j, w in adj[i]:
            dist[i][j] = min(dist[i][j], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    routes = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
    min_cost = float('inf')
    for i in range(n):
        for j in range(n):
            if dist[i][j] < float('inf'):
                cost = 0
                for a, b in routes:
                    cost += dist[a][b]
                min_cost = min(min_cost, cost)
    print(min_cost)

if __name__ == '__main__':
    main()

