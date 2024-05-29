
def solve_chess_board(n):
    board = [['' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = 'W'

    return board

n = int(input())
board = solve_chess_board(n)
for row in board:
    print("".join(row))
```
