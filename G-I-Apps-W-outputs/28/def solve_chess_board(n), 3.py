
def solve_chess_board(n):
    board = []
    
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:
                row.append('B')
            else:
                row.append('W')
        board.append(row)
    
    for row in board:
        print(''.join(row))

n = int(input())
solve_chess_board(n)
```
