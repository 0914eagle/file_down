
def solve(n, m, grid):
    snakes = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                symbol = grid[i][j]
                if i + 1 < n and grid[i+1][j] == symbol:
                    k = i + 1
                    while k < n and grid[k][j] == symbol:
                        k += 1
                    snakes.append((i+1, j+1, k, j+1))
                elif j + 1 < m and grid[i][j+1] == symbol:
                    k = j + 1
                    while k < m and grid[i][k] == symbol:
                        k += 1
                    snakes.append((i+1, j+1, i+1, k))
    return snakes

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    snakes = solve(n, m, grid)
    if len(snakes) > 26:
        print("NO")
    else:
        print("YES")
        print(len(snakes))
        for snake in snakes:
            print(*snake)

