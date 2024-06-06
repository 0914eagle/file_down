
#python3

n = int(input())
grid = []

for i in range(n):
    grid.append(input())

visited = [[False for j in range(n)] for i in range(n)]

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return

    if visited[i][j] or grid[i][j] == 'E':
        return

    visited[i][j] = True

    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

dfs(0, 0)

for i in range(n):
    for j in range(n):
        if visited[i][j] and grid[i][j] == '.':
            print(-1)
            exit()

start_cell = None

for i in range(n):
    for j in range(n):
        if visited[i][j] and grid[i][j] == 'E':
            start_cell = (i, j)

path = []

def purify(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return

    if grid[i][j] == 'E':
        path.append([i, j])
        grid[i][j] = '.'

    purify(i+1, j)
    purify(i-1, j)
    purify(i, j+1)
    purify(i, j-1)

purify(start_cell[0], start_cell[1])

print(len(path))
for cell in path:
    print(cell[0]+1, cell[1]+1)
