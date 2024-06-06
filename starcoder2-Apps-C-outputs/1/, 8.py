
# 100%

r, c = map(int, input().split())

board = []
for i in range(r):
    board.append(list(input()))

target = []
for i in range(r):
    target.append(list(input()))

def hammer(board, i, j):
    board[i][j] = 'O' if board[i][j] == 'X' else 'X'
    for k in range(c):
        board[i][k] = 'O' if board[i][k] == 'X' else 'X'
    for k in range(r):
        board[k][j] = 'O' if board[k][j] == 'X' else 'X'

def check(board, target):
    for i in range(r):
        for j in range(c):
            if board[i][j] != target[i][j]:
                return False
    return True

def dfs(board, target, i, j):
    if i == r:
        return check(board, target)
    if j == c:
        return dfs(board, target, i + 1, 0)
    if board[i][j] == target[i][j]:
        return dfs(board, target, i, j + 1)
    hammer(board, i, j)
    if dfs(board, target, i, j + 1):
        return True
    hammer(board, i, j)
    return False

print(1 if dfs(board, target, 0, 0) else 0)
