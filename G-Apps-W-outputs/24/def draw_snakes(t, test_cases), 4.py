
def draw_snakes(t, test_cases):
    def dfs(i, j, char):
        nonlocal curr_snake
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or grid[i][j] != char:
            return
        
        visited[i][j] = True
        snake[curr_snake].append((i, j))
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(i + x, j + y, char)
    
    def check_snake_shape(s):
        if len(s) == 1:
            return "1x1"
        elif s[0][0] == s[1][0]:
            return f"1x{abs(s[0][1] - s[1][1]) + 1}"
        else:
            return f"{abs(s[0][0] - s[1][0]) + 1}x1"
    
    result = []
    for case in test_cases:
        n, m = case[0]
        grid = case[1]
        visited = [[False]*m for _ in range(n)]
        snake = {}
        curr_snake = 0
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] != '.':
                    char = grid[i][j]
                    snake[curr_snake] = []
                    dfs(i, j, char)
                    curr_snake += 1
        
        snakes_coords = []
        for i in range(curr_snake):
            snake_shape = check_snake_shape(snake[i])
            if snake_shape != "1x1":
                snakes_coords.append((snake[i][0][0]+1, snake[i][0][1]+1, snake[i][-1][0]+1, snake[i][-1][1]+1))
        
        if len(snakes_coords) == 0:
            result.append("YES\n0")
        else:
            result.append("YES")
            result.append(str(len(snakes_coords)))
            for coords in snakes_coords:
                result.append(" ".join(map(str, coords)))
    
    return result

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    test_cases.append(((n, m), grid))

# Call the function and print the results
results = draw_snakes(t, test_cases)
for res in results:
    print(res)
