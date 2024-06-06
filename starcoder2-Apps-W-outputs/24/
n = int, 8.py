
n = int(input())

board = []

for i in range(n):
    row = []
    for j in range(n):
        if (i + j) % 2 == 0:
            row.append('W')
        else:
            row.append('B')
    board.append(row)

for i in range(n):
    print(''.join(board[i]))
