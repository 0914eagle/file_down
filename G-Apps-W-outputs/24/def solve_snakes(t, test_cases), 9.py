
def solve_snakes(t, test_cases):
    def find_next_empty_cell(grid, visited):
        for i in range(len(grid)):
            for j in range(len(grid[0]):
                if grid[i][j] == '.' and not visited[i][j]:
                    return i, j
        return -1, -1
    
    def draw_snake(grid, r1, c1, r2, c2, symbol):
        for i in range(min(r1, r2), max(r1, r2)+1):
            for j in range(min(c1, c2), max(c1, c2)+1):
                grid[i][j] = symbol
    
    def check_valid_snake(grid, r1, c1, r2, c2, symbol):
        for i in range(min(r1, r2), max(r1, r2)+1):
            for j in range(min(c1, c2), max(c1, c2)+1):
                if grid[i][j] != '.' and grid[i][j] != symbol:
                    return False
        return True
    
    def solve_test_case(n, m, grid):
        visited = [[False for _ in range(m)] for _ in range(n)]
        snakes = []
        
        for symbol in range(97, 123):  # ASCII values for lowercase letters a to z
            r, c = find_next_empty_cell(grid, visited)
            if r == -1:  # No more empty cells left
                break
            
            r1, c1, r2, c2 = r, c, r, c
            while r2 < n and grid[r2][c] == '.' and not visited[r2][c]:
                r2 += 1
            while c2 < m and grid[r][c2] == '.' and not visited[r][c2]:
                c2 += 1
            
            if r2 - r1 > 1 or c2 - c1 > 1:
                return 'NO'
            
            if not check_valid_snake(grid, r1, c1, r2, c2, chr(symbol)):
                return 'NO'
            
            draw_snake(grid, r1, c1, r2, c2, chr(symbol))
            visited[r1][c1] = True
            snakes.append((r1+1, c1+1, r2+1, c2+1))
        
        return 'YES', snakes
    
    results = []
    for i in range(t):
        n, m = test_cases[i][0]
        grid = test_cases[i][1]
        result = solve_test_case(n, m, grid)
        results.append(result)
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    test_cases.append((n, m, grid))

# Solve test cases
results = solve_snakes(t, test_cases)

# Output results
for result in results:
    print(result[0])
    if result[0] == 'YES':
        print(len(result[1]))
        for snake in result[1]:
            print(*snake)
