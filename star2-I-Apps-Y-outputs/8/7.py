
def is_valid(x, y, n):
    if x < 1 or x > n or y < 1 or y > n:
        return False
    return True


def bfs(x, y, n, board):
    visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    queue = [(x, y, 0)]
    visited[x][y] = True
    while queue:
        x, y, dist = queue.pop(0)
        if x == 1 and y == 1:
            return dist
        for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, n) and not visited[nx][ny] and board[nx][ny] == '.':
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    return -1


n = int(input())
board = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 'K':
            x, y = i, j
print(bfs(x, y, n, board))

