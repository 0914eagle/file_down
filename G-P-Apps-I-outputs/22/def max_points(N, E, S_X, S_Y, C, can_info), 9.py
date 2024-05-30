
def max_points(N, E, S_X, S_Y, C, can_info):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    for x, y, ct in can_info:
        grid[y][x] = ct

    points = 0
    for t in range(1, 101):
        if E <= 0:
            break

        if grid[S_Y][S_X] == t:
            points += 1
            E += 1

        adjacent_cells = [(S_X, S_Y-1), (S_X, S_Y+1), (S_X-1, S_Y), (S_X+1, S_Y)]
        for adj_x, adj_y in adjacent_cells:
            if 0 <= adj_x < N and 0 <= adj_y < N and grid[adj_y][adj_x] == t:
                E += 1

        if S_X < N - 1:
            S_X += 1
        elif S_Y < N - 1:
            S_X = 0
            S_Y += 1

        E -= 1

    return points

# Input parsing
N, E, S_X, S_Y, C = map(int, input().split())
can_info = [list(map(int, input().split())) for _ in range(C)]

print(max_points(N, E, S_X, S_Y, C, can_info))
```
