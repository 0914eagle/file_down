
def find_tour(N, M):
    if N * M % 2 == 1:
        return -1

    tour = []
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < M

    def backtrack(x, y, idx):
        tour.append((x, y))
        if idx == N * M - 1:
            return True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid(nx, ny):
                tour.append((nx, ny))
                if backtrack(nx, ny, idx + 1):
                    return True
                tour.pop()

        return False

    for i in range(N):
        for j in range(M):
            tour = []
            if backtrack(i, j, 0):
                return tour

    return -1

N, M = map(int, input().split())
result = find_tour(N, M)
if result == -1:
    print(-1)
else:
    for row, col in result:
        print(row + 1, col + 1)
```
