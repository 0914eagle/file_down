
def calculate_min_distances(n, coordinates, speeds):
    coordinates.sort()
    total_distance = 0
    
    for i in range(n):
        for j in range(i+1, n):
            displace = (coordinates[j] - coordinates[i]) / (speeds[i] - speeds[j])
            if displace >= 0:
                min_distance = min(abs((coordinates[i] + speeds[i] * displace) - (coordinates[j] + speeds[j] * displace)), 
                                   abs(coordinates[i] - coordinates[j]))
                total_distance += min_distance
    
    return total_distance

# Input
n = int(input())
coordinates = list(map(int, input().split()))
speeds = list(map(int, input().split()))

# Output
print(calculate_min_distances(n, coordinates, speeds))
```
