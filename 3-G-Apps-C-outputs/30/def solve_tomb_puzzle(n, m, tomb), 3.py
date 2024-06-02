
def solve_tomb_puzzle(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def rotate_gargoyle(gargoyles, x, y, direction):
        if gargoyles[x][y] == 'V':
            if direction == 'left':
                gargoyles[x][y] = '>'
            elif direction == 'right':
                gargoyles[x][y] = '<'
        elif gargoyles[x][y] == 'H':
            if direction == 'up':
                gargoyles[x][y] = 'v'
            elif direction == 'down':
                gargoyles[x][y] = '^'

    def get_next_cell(x, y, direction):
        if direction == 'up':
            return x - 1, y
        elif direction == 'down':
            return x + 1, y
        elif direction == 'left':
            return x, y - 1
        elif direction == 'right':
            return x, y + 1

    def follow_beam(x, y, direction):
        visited = set()
        while is_valid(x, y) and tomb[x][y] != '#':
            if (x, y) in visited:
                return False
            visited.add((x, y))

            if tomb[x][y] == 'V' or tomb[x][y] == 'H':
                rotate_gargoyle(gargoyles, x, y, direction)
                return True

            if tomb[x][y] == '/':
                if direction == 'up':
                    direction = 'right'
                elif direction == 'down':
                    direction = 'left'
                elif direction == 'left':
                    direction = 'down'
                elif direction == 'right':
                    direction = 'up'
            elif tomb[x][y] == '\\':
                if direction == 'up':
                    direction = 'left'
                elif direction == 'down':
                    direction = 'right'
                elif direction == 'left':
                    direction = 'up'
                elif direction == 'right':
                    direction = 'down'

            x, y = get_next_cell(x, y, direction)

        return False

    gargoyles = [list(row) for row in tomb]
    rotations = 0

    for i in range(n):
        for j in range(m):
            if tomb[i][j] == 'V' or tomb[i][j] == 'H':
                if follow_beam(i, j, 'up'):
                    rotations += 1

    return rotations if all(g == '.' for row in gargoyles for g in row) else -1

# Read input
n, m = map(int, input().split())
tomb = [input() for _ in range(n)]

# Solve the tomb puzzle
result = solve_tomb_puzzle(n, m, tomb)
print(result)
