
from collections import deque

def min_knight_steps(board):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                queue.append((i, j, 0))
                visited[i][j] = True
                break
        else:
            continue
        break
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    while queue:
        row, col, steps = queue.popleft()
        if row == 0 and col == 0:
            return steps
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < n and 0 <= new_col < n and not visited[new_row][new_col] and board[new_row][new_col] != '#':
                queue.append((new_row, new_col, steps + 1))
                visited[new_row][new_col] = True
    return -1

n = int(input())
board = [input() for _ in range(n)]
print(min_knight_steps(board))

