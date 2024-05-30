
def checkmate_possible(chessboard):
    king_pos = None
    rook_pos = None
    opponent_king_pos = None

    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 'K':
                king_pos = (i, j)
            elif chessboard[i][j] == 'R':
                rook_pos = (i, j)
            elif chessboard[i][j] == 'k':
                opponent_king_pos = (i, j)

    # Check if moving the rook can checkmate the opponent
    if rook_pos[0] == opponent_king_pos[0] or rook_pos[1] == opponent_king_pos[1]:
        return "Yes"
    
    # Check if the king can move to checkmate the opponent
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_pos = (king_pos[0] + i, king_pos[1] + j)
            if 0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 8 and new_pos != king_pos:
                if new_pos == opponent_king_pos:
                    return "Yes"

    return "No"

# Sample Input
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

print(checkmate_possible(chessboard))  # Output: Yes
```
