
def calculate_valera_positions(a, d, n):
    x = 0.0
    y = 0.0
    positions = []
    
    for i in range(1, n+1):
        if x == 0.0:
            if y + d <= a:
                y += d
            else:
                x = a - (d - (a - y))
                y = a
        elif y == a:
            if x + d <= a:
                x += d
            else:
                y = a - (d - (a - x))
                x = 0
        elif x == a:
            if y - d >= 0:
                y -= d
            else:
                x = d - y
                y = 0
        else:
            if x - d >= 0:
                x -= d
            else:
                y = d - x
                x = 0
        
        positions.append((round(x, 10), round(y, 10)))
    
    return positions

# Input
a, d = map(float, input().split())
n = int(input())

# Calculate and output Valera's positions
positions = calculate_valera_positions(a, d, n)
for pos in positions:
    print("{:.10f} {:.10f}".format(pos[0], pos[1]))
