
def clean_ice(rink_rows, rink_cols, zamboni_row, zamboni_col, num_steps):
    ice_rink = [['.' for _ in range(rink_cols)] for _ in range(rink_rows)]
    color = 'A'
    current_row = zamboni_row - 1
    current_col = zamboni_col - 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, down, left, up
    direction_index = 0
    for step in range(num_steps):
        step_size = step + 1
        for _ in range(step_size):
            current_row += directions[direction_index][0]
            current_col += directions[direction_index][1]
            if ice_rink[current_row][current_col] != '.':
                color = chr(ord(color) + 1)
            ice_rink[current_row][current_col] = color
        direction_index = (direction_index + 1) % len(directions)
    ice_rink[zamboni_row - 1][zamboni_col - 1] = '@'
    return ice_rink


rink_rows, rink_cols, zamboni_row, zamboni_col, num_steps = map(int, input().split())
ice_rink = clean_ice(rink_rows, rink_cols, zamboni_row, zamboni_col, num_steps)
for row in ice_rink:
    print(''.join(row))

