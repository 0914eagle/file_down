
import sys

def solve(n, m, x1, y1, x2, y2, x3, y3, x4, y4):
    white_cells = (x2 - x1 + 1) * (y2 - y1 + 1)
    black_cells = (x4 - x3 + 1) * (y4 - y3 + 1)
    white_cells -= (min(x2, x4) - max(x1, x3) + 1) * (min(y2, y4) - max(y1, y3) + 1)
    black_cells -= white_cells
    return white_cells, black_cells

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
        white_cells, black_cells = solve(n, m, x1, y1, x2, y2, x3, y3, x4, y4)
        print(white_cells, black_cells)

