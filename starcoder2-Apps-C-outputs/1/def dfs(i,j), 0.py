
import sys
sys.setrecursionlimit(10000000)

def dfs(i,j):
    if i == r and j == c:
        return True
    if i > r or j > c:
        return False
    if board[i][j] == 0:
        return False
    board[i][j] = 0
    if dfs(i+1,j) or dfs(i,j+1):
        return True
    board[i][j] = 1
    return False

r,c = map(int,input().split())
board = [[0]*(c+1) for _ in range(r+1)]
for i in range(1,r+1):
    s = input()
    for j in range(1,c+1):
        if s[j-1] == 'O':
            board[i][j] = 1
for i in range(1,r+1):
    s = input()
    for j in range(1,c+1):
        if s[j-1] == 'O':
            board[i][j] = 1

print(dfs(1,1))
