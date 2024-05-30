
def can_checkmate(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                rook_row = i
                rook_col = j
            if board[i][j] == 'K':
                king_row = i
                king_col = j

    opponent_king_row, opponent_king_col = 0, 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'k':
                opponent_king_row = i
                opponent_king_col = j

    # Check if rook can capture opponent's king
    if rook_row == opponent_king_row or rook_col == opponent_king_col:
        return "Yes"

    return "No"

# Read input board
board = []
for _ in range(8):
    board.append(list(input().strip()))

result = can_checkmate(board)
print(result)
```
