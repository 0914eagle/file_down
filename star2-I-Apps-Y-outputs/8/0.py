
def solve(board, N):
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = [(0, 0)]
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != '#' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist[N-1][N-1]

N = int(input())
board = [input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] == 'K':
            start = (i, j)

print(solve(board, N))

