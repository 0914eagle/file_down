
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    ice_rink[i - 1][j - 1] = '@'

    current_color = 'A'
    direction_idx = 3
    step_size = 1

    steps_taken = 0
    while steps_taken < n:
        for _ in range(step_size):
            i = (i + directions[direction_idx][0]) % r
            j = (j + directions[direction_idx][1]) % c

            if ice_rink[i][j] == '.':
                ice_rink[i][j] = current_color
            elif ice_rink[i][j] != '@':
                current_color = chr((ord(ice_rink[i][j]) - ord('A') + 1) % 26 + ord('A'))
                ice_rink[i][j] = current_color

        direction_idx = (direction_idx + 1) % 4
        step_size += 1
        steps_taken += step_size

    for row in ice_rink:
        print(''.join(row))

# Input processing
input_str = input()
r, c, i, j, n = map(int, input_str.strip().split())

clean_ice_rink(r, c, i, j, n)
