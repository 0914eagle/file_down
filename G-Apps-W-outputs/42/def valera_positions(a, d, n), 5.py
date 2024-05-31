
def valera_positions(a, d, n):
    x = 0
    y = 0
    positions = []
    for i in range(1, n+1):
        x += d
        x %= (4*a)
        if x <= a:
            y = x
        elif x <= 2*a:
            y = a
            x = 2*a - x
        elif x <= 3*a:
            y = a - (x - 2*a)
            x = 0
        else:
            y = 0
            x = x - 3*a
        positions.append((round(x, 10), round(y, 10))
    
    return positions

# Input
a, d = map(float, input().split())
n = int(input())

# Output
positions = valera_positions(a, d, n)
for pos in positions:
    print(f"{pos[0]:.10f} {pos[1]:.10f}")
