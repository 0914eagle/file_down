
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    ice_rink[i-1][j-1] = '@'

    current_color = 0
    current_direction = 3  # up
    step_size = 1

    steps_taken = 0
    current_row, current_col = i-1, j-1

    while steps_taken < n:
        for _ in range(step_size):
            current_row = (current_row + directions[current_direction][0]) % r
            current_col = (current_col + directions[current_direction][1]) % c
            ice_rink[current_row][current_col] = colors[current_color]

        current_direction = (current_direction + 1) % 4
        current_color = (current_color + 1) % 26
        step_size += 1
        steps_taken += 1

    for row in ice_rink:
        print(''.join(row))

# Input
input_str = input().strip()
r, c, i, j, n = map(int, input_str.split())

# Output
clean_ice_rink(r, c, i, j, n)
