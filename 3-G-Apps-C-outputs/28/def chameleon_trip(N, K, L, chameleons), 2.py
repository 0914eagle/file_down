
def chameleon_trip(N, K, L, chameleons):
    distances = [0] * K
    colors = [i for i in range(K)]
    
    for i in range(N):
        d, color, direction = chameleons[i]
        if direction == 'L':
            direction = -1
        else:
            direction = 1
        
        distances[color] += L - d
        
        for j in range(i+1, N):
            next_d, next_color, next_direction = chameleons[j]
            if next_direction == 'L':
                next_direction = -1
            else:
                next_direction = 1
            
            time_to_meet = (next_d - d) / 2
            distances[color] += time_to_meet
            
            if color != next_color:
                colors[color] = (colors[color] + colors[next_color]) % K
                color = next_color
            
            d = next_d
            if direction == next_direction:
                distances[color] += L - d
                break
        
    return distances

# Input
N, K, L = map(int, input().split())
chameleons = []
for _ in range(N):
    d, color, direction = input().split()
    chameleons.append((int(d), int(color), direction))

# Output
result = chameleon_trip(N, K, L, chameleons)
for distance in result:
    print("{:.1f}".format(distance))
