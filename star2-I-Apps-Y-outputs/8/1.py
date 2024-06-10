
from collections import deque
def solve(board):
    n = len(board)
    queue = deque()
    queue.append(((0, 0), 0))
    visited = set()
    while queue:
        pos, steps = queue.popleft()
        if pos == (n - 1, n - 1):
            return steps
        if pos in visited:
            continue
        visited.add(pos)
        for i in range(8):
            new_pos = (pos[0] + moves[i][0], pos[1] + moves[i][1])
            if 0 <= new_pos[0] < n and 0 <= new_pos[1] < n and board[new_pos[0]][new_pos[1]] != '#' and new_pos not in visited:
                queue.append((new_pos, steps + 1))
    return -1
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
n = int(input())
board = []
for _ in range(n):
    board.append(input())
for i in range(n):
    for j in range(n):
        if board[i][j] == 'K':
            knight_pos = (i, j)
print(solve(board))

