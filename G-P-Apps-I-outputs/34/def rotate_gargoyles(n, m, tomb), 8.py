
def rotate_gargoyles(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def dfs(x, y, direction):
        if not is_valid(x, y) or tomb[x][y] == '#':
            return
        if visited[x][y][direction]:
            return
        visited[x][y][direction] = True

        if tomb[x][y] in ['V', 'H']:
            if tomb[x][y] == 'V':
                if direction == 'up':
                    dfs(x - 1, y, 'down')
                elif direction == 'down':
                    dfs(x + 1, y, 'up')
            else:
                if direction == 'left':
                    dfs(x, y - 1, 'right')
                elif direction == 'right':
                    dfs(x, y + 1, 'left')

        if tomb[x][y] in ['\\', '/']:
            if tomb[x][y] == '\\':
                if direction == 'up':
                    dfs(x, y + 1, 'right')
                elif direction == 'down':
                    dfs(x, y - 1, 'left')
                elif direction == 'left':
                    dfs(x + 1, y, 'down')
                elif direction == 'right':
                    dfs(x - 1, y, 'up')
            else:  # '/'
                if direction == 'up':
                    dfs(x, y - 1, 'left')
                elif direction == 'down':
                    dfs(x, y + 1, 'right')
                elif direction == 'left':
                    dfs(x - 1, y, 'up')
                elif direction == 'right':
                    dfs(x + 1, y, 'down')

        dfs(x - 1, y, 'up')
        dfs(x + 1, y, 'down')
        dfs(x, y - 1, 'left')
        dfs(x, y + 1, 'right')

    def count_gargoyles():
        count = 0
        for i in range(n):
            for j in range(m):
                if tomb[i][j] in ['V', 'H']:
                    count += 1
        return count

    visited = [[[False, False, False, False] for _ in range(m)] for _ in range(n)]
    gargoyles = count_gargoyles()
    rotations = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j][0] and tomb[i][j] != '#' and tomb[i][j] in ['V', 'H']:
                dfs(i, j, 'up')
                rotations += 1

    if sum(sum(sum(v) for v in row) for row in visited) < gargoyles * 4:
        return -1

    return rotations

# Reading input
n, m = map(int, input().split())
tomb = [input() for _ in range(n)]

# Output result
print(rotate_gargoyles(n, m, tomb))
```
