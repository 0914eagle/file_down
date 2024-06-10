
def solve(n, m, grid):
    snakes = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                snake_symbol = grid[i][j]
                snake_length = 1
                for k in range(j+1, m):
                    if grid[i][k] == snake_symbol:
                        snake_length += 1
                    else:
                        break
                for k in range(i+1, n):
                    if grid[k][j] == snake_symbol:
                        snake_length += 1
                    else:
                        break
                snakes.append((i+1, j+1, i+1, j+snake_length))
    return snakes


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [input() for _ in range(n)]
        snakes = solve(n, m, grid)
        print("YES")
        print(len(snakes))
        for snake in snakes:
            print(*snake)


if __name__ == "__main__":
    main()

