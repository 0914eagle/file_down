
def king_moves(position):
    col = ord(position[0]) - ord('a') + 1
    row = int(position[1])
    
    moves = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 1 <= col + i <= 8 and 1 <= row + j <= 8:
                moves += 1
    
    return moves

position = input().strip()
print(king_moves(position))
```
