
def count_ways_to_drop_piece(C, P, heights):
    def rotate_piece(piece):
        return list(zip(*piece[::-1]))  # Rotate the piece 90 degrees clockwise

    def is_valid_position(field, piece, row, col):
        for r in range(len(piece)):
            for c in range(len(piece[0])):
                if piece[r][c] == 1:
                    if row + r >= len(field) or col + c < 0 or col + c >= len(field[0]):
                        return False
                    if field[row + r][col + c] == 1:
                        return False
        return True

    def drop_piece(field, piece, col):
        row = 0
        while is_valid_position(field, piece, row, col):
            row += 1
        row -= 1
        for r in range(len(piece)):
            for c in range(len(piece[0])):
                if piece[r][c] == 1:
                    field[row + r][col + c] = 1
        return field

    def count_ways(field, piece):
        ways = 0
        for c in range(len(field[0])):
            if is_valid_position(field, piece, 0, c):
                new_field = drop_piece([row[:] for row in field], piece, c)
                ways += count_ways(new_field, piece)
        return 1 if ways == 0 else ways

    pieces = {
        1: [[1]],
        2: [[1, 1]],
        3: [[1, 1, 1]],
        4: [[1, 0], [1, 1]],
        5: [[0, 1], [1, 1]],
        6: [[1, 1], [1, 1]],
        7: [[1, 1, 1], [0, 1, 0]]
    }

    piece = pieces[P]
    ways = count_ways([heights[:] for _ in range(len(piece))], piece)
    return ways

# Read input
C, P = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate and print the number of ways to drop the piece in the field
print(count_ways_to_drop_piece(C, P, heights))
```
