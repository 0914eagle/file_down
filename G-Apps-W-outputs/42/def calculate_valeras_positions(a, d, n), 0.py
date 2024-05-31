
def calculate_valeras_positions(a, d, n):
    x, y = 0, 0
    positions = []
    
    for i in range(1, n+1):
        x += d
        if x < a:
            positions.append((x, y))
        elif x < 2*a:
            positions.append((a, x-a))
        elif x < 3*a:
            positions.append((3*a-x, a))
        else:
            positions.append((0, 4*a-x))
    
    return positions

# Input
a, d = map(float, input().split())
n = int(input())

# Calculate and output Valera's positions
positions = calculate_valeras_positions(a, d, n)
for pos in positions:
    print("{:.10f} {:.10f}".format(pos[0], pos[1]))
