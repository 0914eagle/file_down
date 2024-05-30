
def checkmate_in_single_move(chessboard):
    # Find the positions of Yraglac's rook, king, and opponent's king
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 'R':
                rook_pos = (i, j)
            elif chessboard[i][j] == 'K':
                king_pos = (i, j)
            elif chessboard[i][j] == 'k':
                opponent_king_pos = (i, j)
    
    # Check if moving the rook to opponent's king position will result in checkmate
    if rook_pos[0] == opponent_king_pos[0] or rook_pos[1] == opponent_king_pos[1]:
        return "Yes"
    else:
        return "No"

# Input chessboard as a list of strings
chessboard = [
    "........",
    "........",
    "........",
    "........",
    ".....K.k",
    "........",
    "........",
    "R.......",
]

print(checkmate_in_single_move(chessboard))
```
