
def solve_tomb_puzzle(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def can_see_mirror(x, y, dx, dy):
        while is_valid(x, y):
            if tomb[x][y] == '#':
                return False
            if tomb[x][y] in ['V', 'H']:
                return True
            x += dx
            y += dy
        return False

    def can_unlock_treasure():
        for i in range(n):
            for j in range(m):
                if tomb[i][j] in ['V', 'H']:
                    if tomb[i][j] == 'V':
                        if not (can_see_mirror(i-1, j, -1, 0) or can_see_mirror(i+1, j, 1, 0)):
                            return False
                    else:
                        if not (can_see_mirror(i, j-1, 0, -1) or can_see_mirror(i, j+1, 0, 1)):
                            return False
        return True

    def rotate_gargoyle(x, y):
        if tomb[x][y] == 'V':
            tomb[x][y] = 'H'
        else:
            tomb[x][y] = 'V'

    rotations = 0
    for i in range(n):
        for j in range(m):
            if tomb[i][j] in ['V', 'H']:
                original = tomb[i][j]
                rotate_gargoyle(i, j)
                if can_unlock_treasure():
                    rotations += 1
                tomb[i][j] = original

    return rotations if rotations > 0 else -1

# Input parsing
n, m = map(int, input().split())
tomb = [list(input()) for _ in range(n)]

# Solve the tomb puzzle
result = solve_tomb_puzzle(n, m, tomb)
print(result)
