
import sys

def get_next_color(current_color):
    
    if current_color == 'Z':
        return 'A'
    else:
        return chr(ord(current_color) + 1)

def move_zamboni(rink, i, j, direction, num_steps):
    
    current_color = 'A'
    for _ in range(num_steps):
        for _ in range(num_steps):
            if direction == 'up':
                i -= 1
            elif direction == 'down':
                i += 1
            elif direction == 'left':
                j -= 1
            elif direction == 'right':
                j += 1
            rink[i][j] = current_color
            current_color = get_next_color(current_color)
        direction = {
            'up': 'left',
            'down': 'right',
            'left': 'down',
            'right': 'up'
        }[direction]
    return rink

def print_rink(rink):
    
    for row in rink:
        print(''.join(row))

def main():
    r, c, i, j, n = map(int, sys.stdin.readline().split())
    rink = [['.'] * c for _ in range(r)]
    rink[i-1][j-1] = '@'
    rink = move_zamboni(rink, i-1, j-1, 'up', n)
    print_rink(rink)

if __name__ == '__main__':
    main()

