
def max_points(N, E, SX, SY, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    points = 0

    for t in range(1, 101):  # up to 100 seconds
        if E <= 0:
            break

        for x, y, ct in cans:
            if ct == t:
                if grid[x][y] == 0 and (x == SX and y == SY):
                    points += 1
                    E += 1
                elif abs(x - SX) <= 1 and abs(y - SY) <= 1:
                    E += 1

        E -= 1  # moving costs 1 energy
        grid[SX][SY] = 1  # mark current position as visited

    return points

# Input
N, E, SX, SY, C = map(int, input().split())
cans = []
for _ in range(C):
    X, Y, CT = map(int, input().split())
    cans.append((X, Y, CT))

# Output
print(max_points(N, E, SX, SY, C, cans))
