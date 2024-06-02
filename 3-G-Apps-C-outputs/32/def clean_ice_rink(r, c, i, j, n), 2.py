
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    color_index = 0
    step_size = 1
    current_direction = 3  # up
    current_row, current_col = i - 1, j - 1

    for _ in range(n):
        for _ in range(step_size):
            if 0 <= current_row < r and 0 <= current_col < c:
                ice_rink[current_row][current_col] = colors[color_index]
            current_row += directions[current_direction][0]
            current_col += directions[current_direction][1]

        current_direction = (current_direction + 1) % 4
        color_index = (color_index + 1) % 26
        step_size += 1

    ice_rink[i - 1][j - 1] = '@'

    for row in ice_rink:
        print(''.join(row))

# Input
input_values = input().split()
r, c, i, j, n = map(int, input_values)

# Output
clean_ice_rink(r, c, i, j, n)
