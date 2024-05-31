
def solve_snakes(t, test_cases):
    def find_snakes(n, m, grid):
        snakes = []
        snake_count = 0
        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] != '.':
                    symbol = grid[i][j]
                    snake_count += 1
                    start_row, start_col = i, j
                    end_row, end_col = i, j

                    for k in range(j+1, m):
                        if grid[i][k] == symbol:
                            end_col = k
                        else:
                            break

                    for k in range(i+1, n):
                        if grid[k][j] == symbol:
                            end_row = k
                        else:
                            break

                    for x in range(start_row, end_row+1):
                        for y in range(start_col, end_col+1):
                            if grid[x][y] == '.':
                                return "NO"

                    for x in range(start_row, end_row+1):
                        for y in range(start_col, end_col+1):
                            visited[x][y] = True

                    snakes.append((start_row+1, start_col+1, end_row+1, end_col+1))

        return "YES", snake_count, snakes

    results = []
    for i in range(t):
        n, m = test_cases[i][0], test_cases[i][1]
        grid = test_cases[i][2:]
        result = find_snakes(n, m, grid)
        results.append(result)

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = input()
        grid.append(row)
    test_cases.append((n, m, grid))

results = solve_snakes(t, test_cases)
for result in results:
    print(result[0])
    if result[0] == "YES":
        print(result[1])
        for snake in result[2]:
            print(*snake)
