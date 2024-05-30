
import re

def chess_notation(chess_board):
    # Your code starts here
    # You can add more variables if you need
    white_pieces = []
    black_pieces = []
    for i in range(8):
        for j in range(8):
            if chess_board[i][j] == '.':
                continue
            if chess_board[i][j].isupper():
                white_pieces.append(chess_board[i][j])
            else:
                black_pieces.append(chess_board[i][j])
    white_pieces = sorted(white_pieces)
    black_pieces = sorted(black_pieces)
    white_notation = []
    black_notation = []
    for piece in white_pieces:
        if piece == 'P':
            white_notation.append(piece + chr(ord('a') + j))
        else:
            white_notation.append(piece + str(i + 1))
    for piece in black_pieces:
        if piece == 'p':
            black_notation.append(piece + chr(ord('a') + j))
        else:
            black_notation.append(piece + str(i + 1))
    return 'White: ' + ','.join(white_notation) + '\nBlack: ' + ','.join(black_notation)


