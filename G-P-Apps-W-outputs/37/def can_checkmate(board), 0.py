
def can_checkmate(board):
    # Find Yraglac's rook and king positions
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                rook_pos = (i, j)
            elif board[i][j] == 'K':
                king_pos = (i, j)
    
    # Check if rook can attack opponent's king in a single move
    if rook_pos[0] == king_pos[0] or rook_pos[1] == king_pos[1]:
        return "Yes"
    
    return "No"

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

# Checkmate possibility
print(can_checkmate(board))
```
