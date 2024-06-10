
import sys
sys.setrecursionlimit(100000) # required for DFS

def dfs(grid, i, j, time, fish_count):
    if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] < time or grid[i][j] >= time + k or visited[i][j]):
        return
    visited[i][j] = True
    fish_count += 1
    
    dfs(grid, i + 1, j, time, fish_count) # north
    dfs(grid, i - 1, j, time, fish_count) # south
    dfs(grid, i, j + 1, time, fish_count) # east
    dfs(grid, i, j - 1, time, fish_count) # west
    
    return fish_count
    
r, c, k, l = map(int, input().split())
grid = [[0 for j in range(c)] for i in range(r)]
for i in range(r):
    grid[i] = list(map(int, input().split()))
    
visited = [[False for j in range(c)] for i in range(r)]
x0, y0 = map(int, input().split())
fish_count = dfs(grid, x0, y0, 1, 0)

print(fish_count)

