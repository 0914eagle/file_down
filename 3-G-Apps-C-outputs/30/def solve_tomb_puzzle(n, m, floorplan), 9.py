
def solve_tomb_puzzle(n, m, floorplan):
    def is_valid_move(x, y):
        return 0 <= x < n and 0 <= y < m

    def is_mirror(char):
        return char in ['\\', '/']

    def rotate_gargoyle(gargoyle):
        if gargoyle == 'V':
            return 'H'
        elif gargoyle == 'H':
            return 'V'
        else:
            return gargoyle

    def can_see_face(x, y, dx, dy):
        while is_valid_move(x, y):
            if floorplan[x][y] in ['V', 'H']:
                return True
            if floorplan[x][y] == '#':
                return False
            if is_mirror(floorplan[x][y]):
                if floorplan[x][y] == '\\':
                    dx, dy = dy, dx
                else:
                    dx, dy = -dy, -dx
            x += dx
            y += dy
        return False

    def solve():
        rotations = 0
        for i in range(n):
            for j in range(m):
                if floorplan[i][j] in ['V', 'H']:
                    if not can_see_face(i - 1, j, -1, 0) and not can_see_face(i + 1, j, 1, 0) and not can_see_face(i, j - 1, 0, -1) and not can_see_face(i, j + 1, 0, 1):
                        return -1
                    if not can_see_face(i - 1, j, -1, 0) or not can_see_face(i + 1, j, 1, 0) or not can_see_face(i, j - 1, 0, -1) or not can_see_face(i, j + 1, 0, 1):
                        floorplan[i][j] = rotate_gargoyle(floorplan[i][j])
                        rotations += 1
        return rotations

    return solve()


# Input parsing
n, m = map(int, input().split())
floorplan = [list(input()) for _ in range(n)]

# Solve the tomb puzzle
result = solve_tomb_puzzle(n, m, floorplan)
print(result)
