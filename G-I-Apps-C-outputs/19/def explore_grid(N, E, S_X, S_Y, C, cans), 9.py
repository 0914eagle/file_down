
def explore_grid(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    collected = 0

    for t in range(1, 101):
        if E == 0:
            break

        for can in cans:
            X, Y, CT = can
            if CT == t:
                if grid[X][Y] == 1:
                    collected += 1
                elif abs(X - S_X) + abs(Y - S_Y) <= 1:
                    E += 1
                grid[X][Y] = 1

        if S_X > 0:
            S_X -= 1
        if S_Y > 0:
            S_Y -= 1

    return collected

N, E, S_X, S_Y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

result = explore_grid(N, E, S_X, S_Y, C, cans)
print(result)
```
