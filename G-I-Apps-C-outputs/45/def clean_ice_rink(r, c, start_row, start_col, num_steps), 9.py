
def clean_ice_rink(r, c, start_row, start_col, num_steps):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    ice_rink[start_row - 1][start_col - 1] = '@'

    current_color = 'A'
    current_direction = 3  # Up
    step_size = 1

    row, col = start_row - 1, start_col - 1
    for _ in range(num_steps):
        for _ in range(step_size):
            row = (row + directions[current_direction][0]) % r
            col = (col + directions[current_direction][1]) % c
            if ice_rink[row][col] == '.':
                ice_rink[row][col] = current_color
            current_color = colors[(colors.index(current_color) + 1) % 26]

        current_direction = (current_direction + 1) % 4
        step_size += 1

    return '\n'.join([''.join(row) for row in ice_rink])

# Read input
input_str = input()
r, c, start_row, start_col, num_steps = map(int, input_str.split())
output = clean_ice_rink(r, c, start_row, start_col, num_steps)
print(output)
```
