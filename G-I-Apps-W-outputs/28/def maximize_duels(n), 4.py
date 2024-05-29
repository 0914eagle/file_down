
def maximize_duels(n):
    board = [['B' if (i+j) % 2 == 0 else 'W' for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'B':
                board[i][j] = 'W'
            else:
                board[i][j] = 'B'
    
    for row in board:
        print(''.join(row))

n = int(input())
maximize_duels(n)
```
