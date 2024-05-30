
def checkmate_possible(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                if 'k' in board[i][j+1:]:
                    return True
                if 'k' in [row[j] for row in board[i+1:]]:
                    return True
    return False

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

if checkmate_possible(board):
    print("Yes")
else:
    print("No")
```
