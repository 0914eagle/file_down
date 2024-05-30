
def chess_notation(chess_board):
    white_pieces = []
    black_pieces = []
    for i in range(len(chess_board)):
        for j in range(len(chess_board[i])):
            if chess_board[i][j] == '.':
                continue
            elif chess_board[i][j].islower():
                black_pieces.append(chess_board[i][j])
            else:
                white_pieces.append(chess_board[i][j])
    white_pieces.sort()
    black_pieces.sort()
    white_notation = ''
    black_notation = ''
    for i in range(len(white_pieces)):
        if i == 0:
            white_notation += white_pieces[i]
        else:
            white_notation += ',' + white_pieces[i]
    for i in range(len(black_pieces)):
        if i == 0:
            black_notation += black_pieces[i]
        else:
            black_notation += ',' + black_pieces[i]
    return 'White: ' + white_notation + '\nBlack: ' + black_notation

