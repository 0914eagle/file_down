
import sys

r, c, i, j, n = map(int, sys.stdin.read().split())
ice = [['.'] * c for _ in range(r)]
ice[i - 1][j - 1] = '@'

step_size = 1
direction = 0
current_color = 'A'

def move(row, col, step_size, direction):
    if direction == 0:
        return row, col + step_size
    elif direction == 1:
        return row - step_size, col
    elif direction == 2:
        return row, col - step_size
    else:
        return row + step_size, col

def rotate(direction):
    return (direction + 1) % 4

def switch_color(current_color):
    next_color_index = ord(current_color) - ord('A') + 1
    next_color_index = (next_color_index + 1) % 26
    return chr(ord('A') + next_color_index)

for _ in range(n):
    i, j = move(i - 1, j - 1, step_size, direction)
    i = (i + r) % r
    j = (j + c) % c
    ice[i][j] = current_color
    direction = rotate(direction)
    current_color = switch_color(current_color)
    step_size += 1

for row in ice:
    print(''.join(row))


