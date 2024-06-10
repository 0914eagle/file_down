
from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    grid = [stdin.readline().strip() for _ in range(n)]
    max_time = 0
    max_grid = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "X":
                time = max(i, n - i - 1, j, m - j - 1)
                if time > max_time:
                    max_time = time
                    max_grid = [["." for _ in range(m)] for _ in range(n)]
                    max_grid[i][j] = "X"
    print(max_time)
    for row in max_grid:
        print("".join(row))

if __name__ == "__main__":
    solve()

