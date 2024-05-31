
def solve_snakes(t, test_cases):
    for i in range(t):
        n, m, sheet = test_cases[i]
        snakes = {}
        snake_count = 0
        for r in range(n):
            for c in range(m):
                if sheet[r][c] != '.':
                    if sheet[r][c] not in snakes:
                        snakes[sheet[r][c]] = []
                    snakes[sheet[r][c]].append((r, c))

        result = [['.' for _ in range(m)] for _ in range(n)]
        snake_positions = []
        for snake, positions in snakes.items():
            if len(positions) == 1:
                x, y = positions[0]
                result[x][y] = snake
                snake_positions.append((x+1, y+1, x+1, y+1))
            else:
                x1, y1 = positions[0]
                x2, y2 = positions[-1]
                if x1 == x2:
                    for j in range(y1, y2+1):
                        result[x1][j] = snake
                    snake_positions.append((x1+1, y1+1, x2+1, y2+1))
                else:
                    for i in range(x1, x2+1):
                        result[i][y1] = snake
                    snake_positions.append((x1+1, y1+1, x2+1, y1+1))

        if result == sheet:
            print("YES")
            print(len(snake_positions))
            for pos in snake_positions:
                print(*pos)
        else:
            print("NO")

t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    sheet = [list(input().strip()) for _ in range(n)]
    test_cases.append((n, m, sheet))

solve_snakes(t, test_cases)
