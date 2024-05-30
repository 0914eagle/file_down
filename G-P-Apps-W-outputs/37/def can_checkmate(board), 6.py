
def can_checkmate(board):
    king_pos = None
    rook_pos = None

    # Find the positions of the king, rook, and opponent's king
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                king_pos = (i, j)
            elif board[i][j] == 'R':
                rook_pos = (i, j)
            elif board[i][j] == 'k':
                opponent_king_pos = (i, j)

    # Check if the opponent's king can be captured in a single move
    if king_pos[0] == opponent_king_pos[0] or king_pos[1] == opponent_king_pos[1]:
        return True
    if rook_pos[0] == opponent_king_pos[0] or rook_pos[1] == opponent_king_pos[1]:
        return True
    return False

# Input
board = [
    "........",
    "........",
    "........",
    "........",
    ".....K.k",
    "........",
    "........",
    "R......."
]

# Check if Yraglac can checkmate the opponent in a single move
result = can_checkmate(board)

# Output
if result:
    print("Yes")
else:
    print("No")
```
