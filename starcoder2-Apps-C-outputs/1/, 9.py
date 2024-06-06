
# -*- coding: utf-8 -*-


def hammer(x, y):
    global board
    if board[x][y] == 'O':
        board[x][y] = 'X'
    else:
        board[x][y] = 'O'
    for i in range(len(board)):
        if board[i][y] == 'O':
            board[i][y] = 'X'
        else:
            board[i][y] = 'O'
    for i in range(len(board[0])):
        if board[x][i] == 'O':
            board[x][i] = 'X'
        else:
            board[x][i] = 'O'

def check():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != target[i][j]:
                return False
    return True

r, c = map(int, input().split())
board = []
for i in range(r):
    board.append(list(input()))
target = []
for i in range(r):
    target.append(list(input()))

for i in range(r):
    for j in range(c):
        hammer(i, j)
        if check():
            print(1)
            exit()
        hammer(i, j)
print(0)
