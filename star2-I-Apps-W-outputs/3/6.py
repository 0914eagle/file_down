
def solve(n, m, grid):
    snakes = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                if i + 1 < n and grid[i + 1][j] == grid[i][j]:
                    snakes.append((i, j, i + 1, j))
                elif j + 1 < m and grid[i][j + 1] == grid[i][j]:
                    snakes.append((i, j, i, j + 1))
    return snakes


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [input() for _ in range(n)]
        snakes = solve(n, m, grid)
        if len(snakes) == 0:
            print("NO")
        else:
            print("YES")
            print(len(snakes))
            for snake in snakes:
                print(snake[0] + 1, snake[1] + 1, snake[2] + 1, snake[3] + 1)


if __name__ == "__main__":
    main()

