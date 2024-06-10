
import sys
sys.setrecursionlimit(10**6)
def fishing(r, c, k, l, x0, y0, grid):
    def dfs(x, y, t):
        if x < 0 or x >= r or y < 0 or y >= c or t > l or grid[x][y] < t or grid[x][y] >= t + k or (x, y) in seen:
            return 0
        seen.add((x, y))
        ret = 1
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ret += dfs(x + dx, y + dy, t + 1)
        return ret
    seen = set()
    return dfs(x0, y0, 1)

r, c, k, l = map(int, input().split())
x0, y0 = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
print(fishing(r, c, k, l, x0, y0, grid))

