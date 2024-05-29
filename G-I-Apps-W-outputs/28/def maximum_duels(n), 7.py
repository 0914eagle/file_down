
def maximum_duels(n):
    board = [['W' if (i + j) % 2 == 0 else 'B' for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                board[i][j] = 'B' if ((i+j) // 2) % 2 == 0 else 'W'
    for row in board:
        print(''.join(row))

n = int(input())
maximum_duels(n)
```
