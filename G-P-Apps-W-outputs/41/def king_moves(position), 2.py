
def king_moves(position):
    column = position[0]
    row = int(position[1])
    
    possible_moves = 0
    
    if row > 1:
        possible_moves += 1
    if row < 8:
        possible_moves += 1
    if column != 'a':
        possible_moves += 1
    if column != 'h':
        possible_moves += 1
    if row > 1 and column != 'a':
        possible_moves += 1
    if row > 1 and column != 'h':
        possible_moves += 1
    if row < 8 and column != 'a':
        possible_moves += 1
    if row < 8 and column != 'h':
        possible_moves += 1
    
    return possible_moves

position = input().strip()
print(king_moves(position))
```
