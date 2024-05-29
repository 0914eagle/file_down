
def solve_chess_board(n):
    board = [['W' if (i + j) % 2 == 0 else 'B' for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board[i][j] = 'W'
            else:
                board[i][j] = 'B'
    
    return board

n = int(input())
result = solve_chess_board(n)
for row in result:
    print(''.join(row))
