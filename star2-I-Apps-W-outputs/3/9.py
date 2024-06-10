
import sys
from collections import defaultdict

def solve(n, m, grid):
    snakes = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                snakes[grid[i][j]].append((i, j))
    k = len(snakes)
    res = []
    for snake, points in snakes.items():
        r1, c1 = points[0]
        r2, c2 = points[-1]
        res.append((r1, c1, r2, c2))
    return k, res

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [input() for _ in range(n)]
        k, res = solve(n, m, grid)
        print("YES" if k > 0 else "NO")
        if k > 0:
            print(k)
            for r1, c1, r2, c2 in res:
                print(r1+1, c1+1, r2+1, c2+1)

if __name__ == "__main__":
    main()

