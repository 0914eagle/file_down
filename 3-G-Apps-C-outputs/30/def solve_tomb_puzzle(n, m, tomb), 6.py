
def solve_tomb_puzzle(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def rotate_gargoyle(gargoyles, x, y):
        if gargoyles[x][y] == 'V':
            gargoyles[x][y] = 'H'
        else:
            gargoyles[x][y] = 'V'

    def check_path(gargoyles, mirrors, x, y, dx, dy):
        while is_valid(x, y):
            if mirrors[x][y] == '#':
                return False
            if gargoyles[x][y] != '.' and (x != 0 or y != 0):
                return True
            x += dx
            y += dy
        return False

    def solve():
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(n):
            for j in range(m):
                if gargoyles[i][j] != '.':
                    for dx, dy in directions:
                        if check_path(gargoyles, mirrors, i + dx, j + dy, dx, dy) and check_path(gargoyles, mirrors, i - dx, j - dy, -dx, -dy):
                            rotate_gargoyle(gargoyles, i, j)
                            return True
        return False

    gargoyles = [list(row) for row in tomb]
    mirrors = [['#'] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            mirrors[i + 1][j + 1] = tomb[i][j]

    for i in range(n + 2):
        mirrors[i][0] = mirrors[i][m + 1] = '/'
    for j in range(m + 2):
        mirrors[0][j] = mirrors[n + 1][j] = '/'

    rotations = 0
    while solve():
        rotations += 1

    for row in gargoyles:
        if any(gargoyle == 'V' or gargoyle == 'H' for gargoyle in row):
            return -1

    return rotations

# Input
n, m = map(int, input().split())
tomb = [input() for _ in range(n)]

# Output
print(solve_tomb_puzzle(n, m, tomb))
