
def chess(chessboard):
    white = []
    black = []
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == '.':
                continue
            elif chessboard[i][j].islower():
                black.append(chessboard[i][j])
            else:
                white.append(chessboard[i][j])
    white.sort()
    black.sort()
    return 'White: ' + ','.join(white) + '\nBlack: ' + ','.join(black)

