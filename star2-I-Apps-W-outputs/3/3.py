
def solve(n, m, grid):
    snakes = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                snake_symbol = grid[i][j]
                snake_length = 1
                if i < n - 1 and grid[i + 1][j] == snake_symbol:
                    snake_direction = 'down'
                    while i + snake_length < n and grid[i + snake_length][j] == snake_symbol:
                        snake_length += 1
                elif j < m - 1 and grid[i][j + 1] == snake_symbol:
                    snake_direction = 'right'
                    while j + snake_length < m and grid[i][j + snake_length] == snake_symbol:
                        snake_length += 1
                else:
                    snake_direction = 'down'
                snakes.append((snake_symbol, snake_length, snake_direction))
    snakes.sort(key=lambda x: x[0])
    return snakes


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    snakes = solve(n, m, grid)
    print('YES')
    print(len(snakes))
    for snake_symbol, snake_length, snake_direction in snakes:
        if snake_direction == 'down':
            print(1, 1, snake_length, 1)
        else:
            print(1, 1, 1, snake_length)

