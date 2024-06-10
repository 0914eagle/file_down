
import sys
import heapq


def solve(n, m, pos, types, dist):
    heapq.heapify(pos)
    horiz = [[] for _ in range(m+1)]
    vert = [[] for _ in range(m+1)]
    for i in range(n):
        x, y, t = pos[i]
        if abs(x) >= abs(y):
            vert[t].append((x, y))
        else:
            horiz[t].append((x, y))
    for i in range(1, m+1):
        horiz[i].sort()
        vert[i].sort()

    cost = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
    cost[0][0] = 0
    heap = [(0, 0)]
    while heap:
        c, u = heapq.heappop(heap)
        if u == n:
            return c
        for i in range(u, n):
            x, y = pos[i]
            t = types[i]
            for v in range(i+1, n+1):
                if cost[v][t] > c + dist[t][v-1]:
                    cost[v][t] = c + dist[t][v-1]
                    heapq.heappush(heap, (cost[v][t], v))


def main():
    n, m = map(int, input().split())
    pos = []
    types = []
    dist = [[] for _ in range(m+1)]
    for i in range(n):
        x, y, t = map(int, input().split())
        pos.append((x, y))
        types.append(t)
        dist[t].append(abs(x) + abs(y))
    print(solve(n, m, pos, types, dist))


if __name__ == '__main__':
    main()


