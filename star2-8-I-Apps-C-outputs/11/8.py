
r, c, i, j, n = map(int, input().split())
rink = [['.' for _ in range(c)] for _ in range(r)]
rink[i-1][j-1] = '@'
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
step_size = 1
direction = 0
current_color = 'A'
for _ in range(n):
    for _ in range(step_size):
        new_i = (i-1 + dirs[direction][0]) % r
        new_j = (j-1 + dirs[direction][1]) % c
        rink[new_i][new_j] = current_color
        i = new_i + 1
        j = new_j + 1
    direction = (direction + 1) % 4
    step_size += 1
    current_color = chr(ord(current_color) + 1) if current_color != 'Z' else 'A'
for row in rink:
    print(''.join(row))

