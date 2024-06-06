
# -*- coding: utf-8 -*-


n, m = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y] = 1
    
    count = 0
    for i in range(n):
        if board[x][i] == 0:
            count += 1
        if board[i][y] == 0:
            count += 1
    print(count, end=' ')
