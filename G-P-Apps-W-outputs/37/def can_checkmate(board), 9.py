
def can_checkmate(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                for x in range(8):
                    if board[x][j] == '.' or board[x][j] == 'k':
                        return "Yes"
                for y in range(8):
                    if board[i][y] == '.' or board[i][y] == 'k':
                        return "Yes"
    return "No"

# Reading input
board = []
for _ in range(8):
    row = input().strip()
    board.append(row)
    
# Checking if Yraglac can checkmate in a single move
result = can_checkmate(board)
print(result)
```
