

#!/usr/bin/python3
import sys

def find_path(size, matrix):
    for x in range(size):
        if matrix[x][x] == 'E':
            return x+1, x+1
    for x in range(size):
        for y in range(size):
            if matrix[x][y] == 'E' and (matrix[x][x] == '.' or matrix[y][y] == '.'):
                return x+1, y+1
    return -1, -1

if __name__ == '__main__':
    size = int(sys.stdin.readline().strip())
    matrix = [sys.stdin.readline().strip() for i in range(size)]

    x, y = find_path(size, matrix)
    if x == -1:
        print('-1')
    else:
        for i in range(size):
            print('{} {}'.format(x, y))
            matrix[x-1][y-1] = '.'
            x, y = find_path(size, matrix)
            if x == -1:
                break
