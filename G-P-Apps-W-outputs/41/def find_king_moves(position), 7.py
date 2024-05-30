
def find_king_moves(position):
    col = position[0]
    row = int(position[1])
    
    moves = 0
    if col != 'a':
        moves += 1
    if col != 'h':
        moves += 1
    if row != 1:
        moves += 1
    if row != 8:
        moves += 1
    if col != 'a' and row != 1:
        moves += 1
    if col != 'h' and row != 1:
        moves += 1
    if col != 'a' and row != 8:
        moves += 1
    if col != 'h' and row != 8:
        moves += 1
    
    return moves

position = input()
print(find_king_moves(position))
```
