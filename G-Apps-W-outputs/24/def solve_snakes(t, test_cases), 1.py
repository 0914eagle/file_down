
def solve_snakes(t, test_cases):
    for i in range(t):
        n, m = test_cases[i][0], test_cases[i][1]
        grid = test_cases[i][2:]

        snakes = []
        snake_char = ord('a')
        
        for x in range(n):
            for y in range(m):
                if grid[x][y] != '.':
                    if (x == 0 or grid[x-1][y] == '.') and (y == 0 or grid[x][y-1] == '.'):
                        snakes.append((x, y, x, y))
                        grid[x][y] = chr(snake_char)
                        snake_char += 1
        
        possible = True
        for x in range(n):
            for y in range(m):
                if grid[x][y] != '.':
                    if (x == 0 or grid[x-1][y] == '.') and (y == 0 or grid[x][y-1] == '.'):
                        possible = False
        
        if possible:
            print("YES")
            print(len(snakes))
            for snake in snakes:
                print(snake[0]+1, snake[1]+1, snake[2]+1, snake[3]+1)
        else:
            print("NO")

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    test_cases.append((n, m, grid))

# Call the function to solve the problem
solve_snakes(t, test_cases)
