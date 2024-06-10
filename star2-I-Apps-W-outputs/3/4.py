
def solve(n, m, grid):
    snakes = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                snake_symbol = grid[i][j]
                snake_length = 1
                if i + 1 < n and grid[i+1][j] == snake_symbol:
                    snake_direction = 'down'
                    snake_length += 1
                    while i + snake_length < n and grid[i+snake_length][j] == snake_symbol:
                        snake_length += 1
                elif j + 1 < m and grid[i][j+1] == snake_symbol:
                    snake_direction = 'right'
                    snake_length += 1
                    while j + snake_length < m and grid[i][j+snake_length] == snake_symbol:
                        snake_length += 1
                snakes.append((snake_symbol, snake_direction, snake_length))
    snakes.sort(key=lambda x: x[0])
    return snakes


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [input() for _ in range(n)]
        snakes = solve(n, m, grid)
        print('YES')
        print(len(snakes))
        for snake_symbol, snake_direction, snake_length in snakes:
            if snake_direction == 'down':
                print(1, snake_symbol, n, snake_symbol)
            else:
                print(snake_symbol, 1, snake_symbol, m)

