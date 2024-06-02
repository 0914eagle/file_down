
def solve_tomb_puzzle(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def is_mirror(char):
        return char in ['/', '\\']

    def rotate_gargoyle(gargoyle):
        if gargoyle == 'V':
            return 'H'
        elif gargoyle == 'H':
            return 'V'
        else:
            return gargoyle

    def dfs(x, y, direction):
        if not is_valid(x, y) or tomb[x][y] == '#' or visited[x][y]:
            return

        visited[x][y] = True

        if tomb[x][y] in ['V', 'H']:
            if tomb[x][y] != direction:
                rotations_needed.add((x, y))
                tomb[x][y] = rotate_gargoyle(tomb[x][y])

        if tomb[x][y] == '/':
            if direction == 'V':
                dfs(x, y + 1, 'H')
            elif direction == 'H':
                dfs(x - 1, y, 'V')
        elif tomb[x][y] == '\\':
            if direction == 'V':
                dfs(x, y - 1, 'H')
            elif direction == 'H':
                dfs(x + 1, y, 'V')

        dfs(x + 1, y, direction)
        dfs(x - 1, y, direction)
        dfs(x, y + 1, direction)
        dfs(x, y - 1, direction)

    rotations_needed = set()
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and tomb[i][j] in ['V', 'H']:
                dfs(i, j, tomb[i][j])

    for i in range(n):
        for j in range(m):
            if tomb[i][j] in ['V', 'H']:
                return -1

    return len(rotations_needed)

# Input parsing
n, m = map(int, input().split())
tomb = [list(input()) for _ in range(n)]

# Solve the tomb puzzle
result = solve_tomb_puzzle(n, m, tomb)
print(result)
