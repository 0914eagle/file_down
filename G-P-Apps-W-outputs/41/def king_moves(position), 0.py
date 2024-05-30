
def king_moves(position):
    column, row = position
    column_num = ord(column) - ord('a') + 1
    row_num = int(row)
    
    moves = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_column = column_num + i
            new_row = row_num + j
            if 1 <= new_column <= 8 and 1 <= new_row <= 8 and (i != 0 or j != 0):
                moves += 1
    
    return moves

position = input().strip()
print(king_moves(position))
```
