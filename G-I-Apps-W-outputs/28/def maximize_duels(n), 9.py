
def maximize_duels(n):
    board = [['' for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board[i][j] = 'W'
            else:
                board[i][j] = 'B'
    
    return '\n'.join([''.join(row) for row in board])

n = int(input())
print(maximize_duels(n))
```
