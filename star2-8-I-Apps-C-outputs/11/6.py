
import sys

def zamboni(r, c, i, j, n):
    def move(i, j, d, s):
        if d == 0:
            j += s
        elif d == 1:
            i += s
        elif d == 2:
            j -= s
        elif d == 3:
            i -= s

        if j < 1:
            j = c
        elif j > c:
            j = 1
        if i < 1:
            i = r
        elif i > r:
            i = 1

        return i, j

    def rotate(d):
        return (d + 1) % 4

    def nextColor(color):
        if color == 'Z':
            return 'A'
        else:
            return chr(ord(color) + 1)
    ice = [['.' for j in range(c)] for i in range(r)]
    d = 0 # Up
    i, j = i, j
    color = 'A'
    ice[i - 1][j - 1] = color
    for s in range(1, n + 1):
        i, j = move(i, j, d, s)
        d = rotate(d)
        color = nextColor(color)
        ice[i - 1][j - 1] = color
    ice[i - 1][j - 1] = '@'
    return ice

for line in sys.stdin:
    r, c, i, j, n = map(int, line.split())
    ice = zamboni(r, c, i, j, n)
    for row in ice:
        print(''.join(row))

