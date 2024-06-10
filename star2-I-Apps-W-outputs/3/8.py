
import sys
from collections import defaultdict

def solve(n, m, grid):
    snakes = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                snakes[grid[i][j]].append((i, j))
    snakes = sorted(snakes.items(), key=lambda x: len(x[1]), reverse=True)
    snake_coords = []
    for snake, coords in snakes:
        if len(coords) == 1:
            snake_coords.append((coords[0][0] + 1, coords[0][1] + 1, coords[0][0] + 1, coords[0][1] + 1))
        else:
            snake_coords.append((min(c[0] for c in coords) + 1, min(c[1] for c in coords) + 1, max(c[0] for c in coords) + 1, max(c[1] for c in coords) + 1))
    return snake_coords

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [list(input()) for _ in range(n)]
        snake_coords = solve(n, m, grid)
        print("YES")
        print(len(snake_coords))
        for coords in snake_coords:
            print(*coords)

if __name__ == "__main__":
    main()


