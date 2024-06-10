
def solve(n, m, grid):
    pass

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
T, grid = solve(n, m, grid)
print(T)
for row in grid:
    print(row)

