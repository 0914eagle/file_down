
def collect_oil_cans(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    points = 0

    for t in range(1, max(can[2] for can in cans) + 1):
        for can in cans:
            X, Y, CT = can
            if CT == t:
                if (abs(X - S_X) + abs(Y - S_Y)) <= 1:
                    points += 1
                    grid[X][Y] += 1
                else:
                    grid[X][Y] += 1

        if E > 0:
            for x in range(N):
                for y in range(N):
                    if grid[x][y] > 1:
                        points += 1
                        E += grid[x][y] - 1
                        grid[x][y] = 1

        if E > 0:
            if S_X > 0:
                S_X -= 1
                E -= 1
            elif S_X < N - 1:
                S_X += 1
                E -= 1
            elif S_Y > 0:
                S_Y -= 1
                E -= 1
            elif S_Y < N - 1:
                S_Y += 1
                E -= 1

    return points

# Input parsing
N, E, S_X, S_Y, C = map(int, input().split())
cans = []
for _ in range(C):
    X, Y, CT = map(int, input().split())
    cans.append((X, Y, CT))

# Call the function with the input values
result = collect_oil_cans(N, E, S_X, S_Y, C, cans)
print(result)
```
