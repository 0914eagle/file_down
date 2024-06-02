
def chameleon_trip(N, K, L, chameleons):
    distances = [0] * K
    colors = [i for i in range(K)]
    
    for i in range(N):
        d, color, direction = chameleons[i]
        
        if direction == 'D':
            distances[color] += L - d
        else:
            distances[color] += d
    
    for i in range(N-1, -1, -1):
        d, color, direction = chameleons[i]
        
        if direction == 'D':
            distances[color] += d
        else:
            distances[color] += L - d
        
        if i > 0:
            prev_color = chameleons[i-1][1]
            if direction == 'L':
                colors[color] = (colors[color] + colors[prev_color]) % K
            else:
                colors[prev_color] = colors[color]
    
    for color in colors:
        print("{:.1f}".format(distances[color]))

# Input parsing
N, K, L = map(int, input().split())
chameleons = []
for _ in range(N):
    d, color, direction = input().split()
    chameleons.append((int(d), int(color), direction))

# Call the function
chameleon_trip(N, K, L, chameleons)
