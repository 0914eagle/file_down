
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # left, down, right, up
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    
    color = 'A'
    x, y = i - 1, j - 1  # convert 1-based index to 0-based index
    direction = 3  # start facing up
    steps = 1

    for _ in range(n):
        for _ in range(steps):
            ice_rink[x][y] = color
            x = (x + directions[direction][0]) % r
            y = (y + directions[direction][1]) % c

        color = chr((ord(color) - ord('A') + 1) % 26 + ord('A'))
        direction = (direction + 1) % 4
        if steps < min(r, c):
            steps += 1

    ice_rink[x][y] = '@'

    for row in ice_rink:
        print(''.join(row))

# Read input
r, c, i, j, n = map(int, input().split())
clean_ice_rink(r, c, i, j, n)
```
