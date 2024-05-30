
def can_checkmate(board):
    king_position = None
    rook_position = None
    opponent_king_position = None

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                king_position = (i, j)
            elif board[i][j] == 'R':
                rook_position = (i, j)
            elif board[i][j] == 'k':
                opponent_king_position = (i, j)

    # Check if rook can capture opponent's king
    if rook_position[0] == opponent_king_position[0] or rook_position[1] == opponent_king_position[1]:
        return "Yes"

    # Check if king can move to a position to capture opponent's king
    king_moves = [
        (king_position[0] - 1, king_position[1]),  # up
        (king_position[0] + 1, king_position[1]),  # down
        (king_position[0], king_position[1] - 1),  # left
        (king_position[0], king_position[1] + 1),  # right
        (king_position[0] - 1, king_position[1] - 1),  # top-left
        (king_position[0 - 1, king_position[1] + 1),  # top-right
        (king_position[0] + 1, king_position[1] - 1),  # bottom-left
        (king_position[0] + 1, king_position[1] + 1),  # bottom-right
    ]

    if opponent_king_position in king_moves:
        return "Yes"

    return "No"

# Sample Input
board = [
    "........",
    "........",
    "........",
    "........",
    ".....K.k",
    "........",
    "........",
    "R.......",
]

print(can_checkmate(board))
```
