
def valera_positions(a, d, n):
    x, y = 0, 0
    positions = []
    for i in range(1, n + 1):
        if x < a and y == 0:
            dx = min(d, a - x)
            x += dx
        elif x == a and y < a:
            dy = min(d, a - y)
            y += dy
        elif x > 0 and y == a:
            dx = min(d, x)
            x -= dx
        elif x == 0 and y > 0:
            dy = min(d, y)
            y -= dy
        positions.append((round(x, 10), round(y, 10)))
    return positions

# Input
a, d = map(float, input().split())
n = int(input())

# Output
positions = valera_positions(a, d, n)
for pos in positions:
    print('{} {}'.format(pos[0], pos[1]))
