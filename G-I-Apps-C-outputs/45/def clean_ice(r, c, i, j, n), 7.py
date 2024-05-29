
def clean_ice(r, c, i, j, n):
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    ice_rink[i - 1][j - 1] = '@'

    direction_index = 0
    step_size = 1
    color_index = 0

    for _ in range(n):
        for _ in range(step_size):
            i = (i + directions[direction_index][0]) % r
            j = (j + directions[direction_index][1]) % c

            if ice_rink[i][j] == '.':
                ice_rink[i][j] = colors[color_index]
            else:
                color_index = (color_index + 1) % 26
                ice_rink[i][j] = colors[color_index]

        direction_index = (direction_index + 1) % 4
        step_size += 1

    for row in ice_rink:
        print(''.join(row))

# Read input
input_data = input().split()
r, c, i, j, n = map(int, input_data)

# Call the function with input
clean_ice(r, c, i, j, n)
```
