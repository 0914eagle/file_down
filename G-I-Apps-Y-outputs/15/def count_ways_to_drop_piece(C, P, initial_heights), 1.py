
def count_ways_to_drop_piece(C, P, initial_heights):
    def check_valid_column(column):
        for idx in range(len(column)):
            if column[idx] < 0 or column[idx] > C:
                return False
        return True

    def drop_piece_ways(column, piece_height):
        ways = 0
        max_drop = min(column) - piece_height
        for drop in range(-4, max_drop + 1):
            valid_column = [col + drop for col in column]
            if check_valid_column(valid_column):
                ways += 1
        return ways

    pieces = {
        1: [0],
        2: [0, 1],
        3: [-1, 0, 1],
        4: [-1, 0],
        5: [0, -1, 1],
        6: [-1, 0, 1, 2],
        7: [-1, 0, 1, -2],
    }

    ways = 0
    for piece_col in pieces[P]:
        ways += drop_piece_ways(initial_heights, piece_col)
    return ways

# Read input
C, P = map(int, input().split())
initial_heights = list(map(int, input().split()))

# Calculate and print output
print(count_ways_to_drop_piece(C, P, initial_heights))
```
