
def count_king_moves(position):
    col = ord(position[0]) - ord('a') + 1
    row = int(position[1])

    moves = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_col = col + i
            new_row = row + j
            if 1 <= new_col <= 8 and 1 <= new_row <= 8:
                moves += 1

    return moves

position = input().strip()
print(count_king_moves(position))
```
