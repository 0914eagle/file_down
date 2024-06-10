
import sys


def solve(grid):
    for i in range(3):
        for j in range(3):
            if all(c == grid[i][j] for c in grid[i][j:j + 2]) and \
                    all(c == grid[i][j] for c in grid[i + 1][j:j + 2]):
                return "YES"

    return "NO"


def main():
    grid = [list(line.strip()) for line in sys.stdin.read().splitlines()]
    print(solve(grid))


if __name__ == "__main__":
    main()


