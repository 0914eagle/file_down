
def king_moves(position):
    column = position[0]
    row = int(position[1])
    
    moves = 0
    if column != 'a':
        moves += 1
    if column != 'h':
        moves += 1
    if row != 1:
        moves += 1
    if row != 8:
        moves += 1
    if column != 'a' and row != 1:
        moves += 1
    if column != 'h' and row != 1:
        moves += 1
    if column != 'a' and row != 8:
        moves += 1
    if column != 'h' and row != 8:
        moves += 1
    
    return moves

position = input().strip()
print(king_moves(position))
```
