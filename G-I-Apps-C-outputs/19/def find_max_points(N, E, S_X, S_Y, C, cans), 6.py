
def find_max_points(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    points = 0

    for i in range(E):
        for can in cans:
            X, Y, CT = can
            if abs(X - S_X) + abs(Y - S_Y) <= i + CT:
                if X == S_X and Y == S_Y:
                    points += 1
                    E += 1
                else:
                    for dx, dy in directions:
                        new_X, new_Y = S_X + dx, S_Y + dy
                        if 0 <= new_X < N and 0 <= new_Y < N and (X == new_X or Y == new_Y):
                            E += 1

        S_X += directions[i % 4][0]
        S_Y += directions[i % 4][1]

    return points

# Read input
N, E, S_X, S_Y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

# Call the function and output the result
print(find_max_points(N, E, S_X, S_Y, C, cans))
```
