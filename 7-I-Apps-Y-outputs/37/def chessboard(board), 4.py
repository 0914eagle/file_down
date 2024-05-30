
def chessboard(board):
    white = []
    black = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == '.':
                continue
            elif board[i][j].isupper():
                white.append(board[i][j])
            else:
                black.append(board[i][j])
    return 'White: ' + ','.join(white) + '\nBlack: ' + ','.join(black)

