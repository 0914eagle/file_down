
def chameleon_trip(N, K, L, chameleons):
    distances = [0] * K
    colors = [i for i in range(K)]
    
    for i in range(N):
        d, color, direction = chameleons[i]
        if direction == 'D':
            distances[color] += L - d
        else:
            distances[color] += d
    
    for i in range(N-1):
        d1, color1, direction1 = chameleons[i]
        d2, color2, direction2 = chameleons[i+1]
        
        if direction1 == 'D' and direction2 == 'L':
            distances[color1] += L
            distances[color2] += L
            colors[color1] = (colors[color1] + colors[color2]) % K
            colors[color2] = colors[color1]
    
    for i in range(K):
        print("{:.1f}".format(distances[colors[i]]))

# Input parsing
N, K, L = map(int, input().split())
chameleons = []
for _ in range(N):
    d, color, direction = input().split()
    chameleons.append((int(d), int(color), direction))

# Call the function
chameleon_trip(N, K, L, chameleons)
