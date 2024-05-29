
def find_min_depth(grid):
    r, c = len(grid), len(grid[0])
    dp = [[float('inf') for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        dp[i][0] = grid[i][0]
    
    for j in range(1, c):
        for i in range(r):
            dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[(i-1)%r][j-1], dp[(i+1)%r][j-1])
    
    min_depth = min(dp[i][-1] for i in range(r))
    return min_depth

# Sample Input Processing
input_data = 
lines = input_data.strip().split('\n')
r, c = map(int, lines[0].split())
grid = [list(map(int, line.split())) for line in lines[1:]]

result = find_min_depth(grid)
print(result)
```
