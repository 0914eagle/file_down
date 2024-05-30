
def king_moves(position):
    col, row = position[0], int(position[1])
    
    possible_moves = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_col = chr(ord(col) + i)
            new_row = row + j
            if 'a' <= new_col <= 'h' and 1 <= new_row <= 8:
                possible_moves += 1
                
    return possible_moves

position = input().strip()
print(king_moves(position))
```
