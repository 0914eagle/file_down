
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    color_idx = 0
    current_color = colors[color_idx]

    x, y = i - 1, j - 1
    direction_idx = 3  # zamboni is facing up initially
    steps = 1

    for _ in range(n):
        for _ in range(steps):
            x = (x + directions[direction_idx][0]) % r
            y = (y + directions[direction_idx][1]) % c
            ice_rink[x][y] = current_color

        direction_idx = (direction_idx + 1) % 4
        color_idx = (color_idx + 1) % 26
        current_color = colors[color_idx]

        if steps < min(r, c):
            steps += 1

    for i in range(r):
        for j in range(c):
            if i == x and j == y:
                ice_rink[i][j] = '@'

    for row in ice_rink:
        print(''.join(row))


# Reading input
r, c, i, j, n = map(int, input().split())
clean_ice_rink(r, c, i, j, n)
```
