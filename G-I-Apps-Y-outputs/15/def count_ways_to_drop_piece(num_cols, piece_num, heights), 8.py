
def count_ways_to_drop_piece(num_cols, piece_num, heights):
    # Dictionary representing the shape of each piece
    pieces = {
        1: [[1], [1], [1], [1]],
        2: [[1, 1], [1, 1]],
        3: [[1, 1, 1], [0, 1, 0]],
        4: [[1, 1, 0], [0, 1, 1]],
        5: [[0, 1, 1], [1, 1, 0]],
        6: [[1, 0], [1, 0], [1, 1]],
        7: [[0, 1], [0, 1], [1, 1]]
    }

    piece_shape = pieces[piece_num]
    total_ways = 0

    for shift in range(num_cols - len(piece_shape[0]) + 1):
        valid = True

        for col in range(len(piece_shape)):
            for row in range(len(piece_shape[0])):
                if heights[col + shift] + piece_shape[col][row] > max(heights):
                    valid = False
                    break

            if not valid:
                break

        if valid:
            total_ways += 1

    return total_ways

# Input processing
input_line = input().split()
num_cols = int(input_line[0])
piece_num = int(input_line[1])

heights = list(map(int, input().split()))

# Call the function and print the result
print(count_ways_to_drop_piece(num_cols, piece_num, heights))
```
