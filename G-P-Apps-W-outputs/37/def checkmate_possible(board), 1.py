
def checkmate_possible(board):
    king_pos = None
    rook_pos = None

    # Find the positions of Yraglac's king and rook
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                king_pos = (i, j)
            elif board[i][j] == 'R':
                rook_pos = (i, j)

    # Check if moving the rook to the opponent's king position leads to checkmate
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'k':
                if i == rook_pos[0] or j == rook_pos[1]:
                    return "Yes"
                else:
                    return "No"

    return "No"

# Sample input
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

print(checkmate_possible(board))
```
