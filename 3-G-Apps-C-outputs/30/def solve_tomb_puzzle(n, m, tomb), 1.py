
def solve_tomb_puzzle(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def rotate_gargoyle(x, y, direction):
        if tomb[x][y] == 'V':
            if direction == 'left':
                tomb[x][y] = 'H'
            else:
                tomb[x][y] = 'V'
        else:
            if direction == 'up':
                tomb[x][y] = 'V'
            else:
                tomb[x][y] = 'H'

    def dfs(x, y, direction):
        if not is_valid(x, y) or tomb[x][y] == '#' or visited[x][y]:
            return

        visited[x][y] = True

        if tomb[x][y] in ['V', 'H']:
            if (tomb[x][y] == 'V' and direction in ['up', 'down']) or (tomb[x][y] == 'H' and direction in ['left', 'right']):
                rotate_gargoyle(x, y, direction)
                rotations[0] += 1

        if tomb[x][y] in ['V', 'H', '.', '/']:
            if direction == 'up':
                dfs(x - 1, y, 'up')
            elif direction == 'down':
                dfs(x + 1, y, 'down')
            elif direction == 'left':
                dfs(x, y - 1, 'left')
            elif direction == 'right':
                dfs(x, y + 1, 'right')

    rotations = [0]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and tomb[i][j] in ['V', 'H']:
                dfs(i, j, 'up')

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and tomb[i][j] in ['V', 'H']:
                return -1

    return rotations[0]

# Input processing
n, m = map(int, input().split())
tomb = [list(input()) for _ in range(n)]

# Call the function and output the result
result = solve_tomb_puzzle(n, m, tomb)
print(result)
