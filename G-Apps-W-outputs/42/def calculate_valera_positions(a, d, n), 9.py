
def calculate_valera_positions(a, d, n):
    x = 0
    y = 0
    positions = []
    
    for i in range(1, n + 1):
        x += d
        if x < a:
            y = x
        elif x < 2 * a:
            y = a
            x -= a
        elif x < 3 * a:
            y = a - x % a
            x = 0
        else:
            y = 0
            x = a - x % (3 * a)
        
        positions.append((round(x, 10), round(y, 10)))
    
    return positions

# Input
a, d = map(float, input().split())
n = int(input())

# Output
positions = calculate_valera_positions(a, d, n)
for position in positions:
    print("{:.10f} {:.10f}".format(position[0], position[1]))
