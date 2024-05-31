
def valera_positions(a, d, n):
    x, y = 0, 0
    for i in range(1, n+1):
        if x + d <= a:  # moving right
            x += d
        elif x + d > a and y + d <= a:  # moving up
            y += d
        elif y + d > a and x - d >= 0:  # moving left
            x -= d
        elif x - d < 0 and y - d >= 0:  # moving down
            y -= d
        print('{:.10f} {:.10f}'.format(x, y))

a, d = map(float, input().split())
n = int(input())
valera_positions(a, d, n)
