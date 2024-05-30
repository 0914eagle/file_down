
def min_ladder_length(M, N, vault):
    from queue import PriorityQueue

    def dijkstra():
        q = PriorityQueue()
        q.put((0, (0, 0)))
        dist = {(0, 0): 0}

        while not q.empty():
            d, (x, y) = q.get()
            if (x, y) == (M-1, N-1):
                return d
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    nd = max(d, abs(vault[x][y] - vault[nx][ny]))
                    if (nx, ny) not in dist or nd < dist[(nx, ny)]:
                        dist[(nx, ny)] = nd
                        q.put((nd, (nx, ny)))

    return dijkstra()

# Read input
M, N = map(int, input().split())
vault = [list(map(int, input().split())) for _ in range(M)]

# Calculate and print result
result = min_ladder_length(M, N, vault)
print(result)
```
