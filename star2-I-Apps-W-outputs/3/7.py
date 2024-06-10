
def solve(n, m, grid):
    snakes = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                snake_symbol = grid[i][j]
                snake_length = 1
                if i > 0 and grid[i-1][j] == snake_symbol:
                    snake_direction = 'u'
                    while i > 0 and grid[i-1][j] == snake_symbol:
                        snake_length += 1
                        i -= 1
                elif j > 0 and grid[i][j-1] == snake_symbol:
                    snake_direction = 'l'
                    while j > 0 and grid[i][j-1] == snake_symbol:
                        snake_length += 1
                        j -= 1
                else:
                    snake_direction = 'u'
                snakes.append((snake_symbol, snake_length, snake_direction))
    snakes.sort(key=lambda x: x[0])
    return snakes


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    snakes = solve(n, m, grid)
    print('YES')
    print(len(snakes))
    for snake_symbol, snake_length, snake_direction in snakes:
        if snake_direction == 'u':
            print(1, 1, snake_length, 1)
        else:
            print(1, 1, 1, snake_length)

