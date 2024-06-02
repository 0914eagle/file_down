
def solve_tomb_puzzle(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def dfs(x, y, dx, dy):
        if not is_valid(x, y) or tomb[x][y] == '#':
            return False
        if visited[x][y]:
            return True

        visited[x][y] = True
        if tomb[x][y] == 'V' or tomb[x][y] == 'H':
            new_dx, new_dy = 0, 0
            if tomb[x][y] == 'V':
                new_dx = 1
            else:
                new_dy = 1

            if (dx, dy) == (0, 0) or (dx, dy) == (new_dx, new_dy):
                if dfs(x + new_dx, y + new_dy, new_dx, new_dy):
                    return True

            if (dx, dy) == (0, 0) or (dx, dy) == (-new_dx, -new_dy):
                if dfs(x - new_dx, y - new_dy, -new_dx, -new_dy):
                    return True

        if tomb[x][y] == '/':
            new_dx, new_dy = dy, dx
            if dfs(x + new_dx, y + new_dy, new_dx, new_dy):
                return True

        if tomb[x][y] == '\\':
            new_dx, new_dy = -dy, -dx
            if dfs(x + new_dx, y + new_dy, new_dx, new_dy):
                return True

        return False

    visited = [[False for _ in range(m)] for _ in range(n)]
    rotations = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and (tomb[i][j] == 'V' or tomb[i][j] == 'H'):
                if not dfs(i, j, 0, 0):
                    return -1
                rotations += 1

    return rotations

# Read input
n, m = map(int, input().split())
tomb = [input() for _ in range(n)]

# Solve the tomb puzzle
result = solve_tomb_puzzle(n, m, tomb)
print(result)
