
def count_ways_to_drop_piece(C, P, heights):
    piece_1 = [[0, 0, 0],
               [1, 1, 1]]

    piece_2 = [[0, 0, 0],
               [0, 1, 1],
               [1, 1, 0]]

    piece_3 = [[0, 0],
               [1, 1],
               [1, 1]]

    piece_4 = [[0, 1, 0],
               [1, 1, 1]]

    piece_5 = [[1, 0],
               [1, 1],
               [1, 0]]

    piece_6 = [[0, 1],
               [1, 1],
               [0, 1]]

    piece_7 = [[1, 1],
               [1, 1]]

    pieces = [piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7]

    def rotate_piece(piece, degree):
        for _ in range(degree // 90):
            piece = list(zip(*piece[::-1]))
        return piece

    def check_valid_placement(field, piece, row, col):
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if not(0 <= row + i < len(field) and 0 <= col + j < len(field[0])):
                    return False
                if piece[i][j] == 1 and field[row + i][col + j] == 1:
                    return False
        return True

    def place_piece(field, piece, row, col):
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if piece[i][j] == 1:
                    field[row + i][col + j] = 1

    def count_field_configurations(field, piece):
        count = 0
        for i in range(len(field)):
            for j in range(len(field[0])):
                if check_valid_placement(field, piece, i, j):
                    new_field = [row[:] for row in field]
                    place_piece(new_field, piece, i, j)
                    count += 1 + count_field_configurations(new_field, piece)
        return count

    initial_field = [[0] * h for h in heights]
    total_count = 0
    for angle in range(0, 360, 90):
        rotated_piece = rotate_piece(pieces[P-1], angle)
        total_count += count_field_configurations(initial_field, rotated_piece)

    return total_count

# Read input
C, P = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate and print the number of ways to drop the piece
print(count_ways_to_drop_piece(C, P, heights))
```
