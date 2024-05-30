
def chess(board):
    white = []
    black = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == '.':
                continue
            if board[i][j].isupper():
                black.append(board[i][j])
            else:
                white.append(board[i][j])
    white.sort()
    black.sort()
    return 'White: ' + ','.join(white) + '\nBlack: ' + ','.join(black)

