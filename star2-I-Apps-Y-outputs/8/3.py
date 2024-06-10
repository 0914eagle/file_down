
from collections import deque

def bfs(board, N, start, end):
    queue = deque([start])
    visited = set([start])
    steps = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if (r, c) == end:
                return steps
            for r_new, c_new in [(r + 2, c + 1), (r + 2, c - 1), (r - 2, c + 1), (r - 2, c - 1), (r + 1, c + 2), (r + 1, c - 2), (r - 1, c + 2), (r - 1, c - 2)]:
                if 1 <= r_new <= N and 1 <= c_new <= N and board[r_new][c_new] != '#' and (r_new, c_new) not in visited:
                    queue.append((r_new, c_new))
                    visited.add((r_new, c_new))
        steps += 1
    return -1

N = int(input())
board = [input() for _ in range(N)]
start = (0, 0)
end = (1, 1)
for r in range(N):
    for c in range(N):
        if board[r][c] == 'K':
            start = (r + 1, c + 1)
        elif board[r][c] == '.':
            board[r] = board[r][:c] + ' ' + board[r][c + 1:]
        elif board[r][c] == '#':
            board[r] = board[r][:c] + '#' + board[r][c + 1:]

print(bfs(board, N, start, end))

