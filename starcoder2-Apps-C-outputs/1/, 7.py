
r, c = map(int, input().split())

start = []
for i in range(r):
    start.append(input())

target = []
for i in range(r):
    target.append(input())

def hammer(board, x, y):
    board[x][y] = 'O' if board[x][y] == 'X' else 'X'
    for i in range(c):
        board[x][i] = 'O' if board[x][i] == 'X' else 'X'
    for i in range(r):
        board[i][y] = 'O' if board[i][y] == 'X' else 'X'

def check(board, target):
    for i in range(r):
        for j in range(c):
            if board[i][j] != target[i][j]:
                return False
    return True

def solve(board, target):
    if check(board, target):
        return True
    for i in range(r):
        for j in range(c):
            if board[i][j] != target[i][j]:
                hammer(board, i, j)
                if solve(board, target):
                    return True
                hammer(board, i, j)
    return False

if solve(start, target):
    print(1)
else:
    print(0)
