
def place_magnets(n, m, grid):
    rows = [False] * n
    cols = [False] * m
    north_magnets = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                rows[i] = True
                cols[j] = True

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and not rows[i] and not cols[j]:
                return -1
            if grid[i][j] == '.' and not rows[i]:
                north_magnets += 1
            if grid[i][j] == '.' and not cols[j]:
                north_magnets += 1

    return north_magnets

# Input parsing
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Call the function and print the result
result = place_magnets(n, m, grid)
print(result)
