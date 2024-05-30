
def can_checkmate(board):
    # Find the positions of Yraglac's rook, king, and opponent's king
    row_rook, col_rook = None, None
    row_king, col_king = None, None
    row_opp_king, col_opp_king = None, None
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                row_rook, col_rook = i, j
            elif board[i][j] == 'K':
                row_king, col_king = i, j
            elif board[i][j] == 'k':
                row_opp_king, col_opp_king = i, j
    
    # Check if Yraglac's rook can move to threaten the opponent's king
    if row_rook == row_opp_king or col_rook == col_opp_king:
        return "Yes"
    
    return "No"

# Read the input chessboard
board = []
for _ in range(8):
    row = input().strip()
    board.append(row)

# Check if Yraglac can checkmate his opponent in a single move
result = can_checkmate(board)
print(result)
```
