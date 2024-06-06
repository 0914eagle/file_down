
def hammer(x,y):
    for i in range(n):
        if board[i][y] == 'O':
            board[i][y] = 'X'
        else:
            board[i][y] = 'O'
    for i in range(m):
        if board[x][i] == 'O':
            board[x][i] = 'X'
        else:
            board[x][i] = 'O'

n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
target = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] != target[i][j]:
            hammer(i,j)

for i in range(n):
    for j in range(m):
        if board[i][j] != target[i][j]:
            print(0)
            exit()
print(1)
