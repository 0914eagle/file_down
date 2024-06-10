
from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    grid = [stdin.readline().strip() for _ in range(n)]
    max_time = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X':
                max_time = max(max_time, min(i, j, n - i - 1, m - j - 1))
    for i in range(n):
        for j in range(m):
            if abs(i - n // 2) + abs(j - m // 2) <= max_time:
                grid[i] = grid[i][:j] + 'X' + grid[i][j + 1:]
            else:
                grid[i] = grid[i][:j] + '.' + grid[i][j + 1:]
    return max_time, grid


if __name__ == '__main__':
    max_time, grid = solve()
    print(max_time)
    for row in grid:
        print(row)

