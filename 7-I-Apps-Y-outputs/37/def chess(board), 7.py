
import re

def chess(board):
    board = board.replace("+", "")
    board = board.replace("-", "")
    board = board.replace("|", "")
    board = board.replace(":", "")
    board = board.replace(".", "")
    board = board.replace(" ", "")
    board = board.replace("\n", "")

    white_pieces = re.findall(r"[A-Z]", board)
    black_pieces = re.findall(r"[a-z]", board)
    white_pieces = sorted(white_pieces)
    black_pieces = sorted(black_pieces)

    white_pieces_str = ""
    black_pieces_str = ""

    for piece in white_pieces:
        white_pieces_str += piece
        white_pieces_str += board[board.find(piece):board.find(piece) + 2]

    for piece in black_pieces:
        black_pieces_str += piece.upper()
        black_pieces_str += board[board.find(piece):board.find(piece) + 2]

    print("White:", white_pieces_str)
    print("Black:", black_pieces_str)

