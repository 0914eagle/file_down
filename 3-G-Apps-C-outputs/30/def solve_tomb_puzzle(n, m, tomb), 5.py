
def solve_tomb_puzzle(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def rotate_gargoyle(gargoyles, x, y, direction):
        if gargoyles[x][y] == 'V':
            if direction == 'clockwise':
                gargoyles[x][y] = 'H'
            else:
                gargoyles[x][y] = 'V'
        else:
            if direction == 'clockwise':
                gargoyles[x][y] = 'V'
            else:
                gargoyles[x][y] = 'H'

    def check_path(gargoyles, x, y, dx, dy):
        while is_valid(x, y):
            if tomb[x][y] == '#':
                return False
            if gargoyles[x][y] != '.':
                return True
            x += dx
            y += dy
        return False

    def count_rotations(gargoyles):
        rotations = 0
        for i in range(n):
            for j in range(m):
                if gargoyles[i][j] != '.':
                    if not check_path(gargoyles, i - 1, j, -1, 0) and not check_path(gargoyles, i + 1, j, 1, 0) and not check_path(gargoyles, i, j - 1, 0, -1) and not check_path(gargoyles, i, j + 1, 0, 1):
                        return -1
                    if check_path(gargoyles, i - 1, j, -1, 0) and check_path(gargoyles, i + 1, j, 1, 0) and check_path(gargoyles, i, j - 1, 0, -1) and check_path(gargoyles, i, j + 1, 0, 1):
                        continue
                    rotate_gargoyle(gargoyles, i, j, 'clockwise')
                    rotations += 1
        return rotations

    gargoyles = [[c for c in row] for row in tomb]
    rotations = count_rotations(gargoyles)
    return rotations

# Read input
n, m = map(int, input().split())
tomb = [input() for _ in range(n)]

# Solve the tomb puzzle
result = solve_tomb_puzzle(n, m, tomb)
print(result)
