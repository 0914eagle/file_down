
def solve_grid(A, B):
    h = A + 1
    w = B + 1
    grid = [['#' for _ in range(w)] for _ in range(h)]

    for i in range(1, h):
        for j in range(1, w):
            grid[i][j] = '.' if (i+j) % 2 == 0 else '#'

    print(h, w)
    for row in grid:
        print(''.join(row))

# Read input
A, B = map(int, input().split())
solve_grid(A, B)
