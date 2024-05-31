
import math

def is_megacity_possible(n, s, locations):
    total_population = s
    for x, y, k in locations:
        total_population += k

    if total_population >= 1000000:
        return 0.0

    distances = []
    for x, y, k in locations:
        distance = math.sqrt(x**2 + y**2)
        distances.append(distance)

    distances.sort()
    for i in range(n):
        total_population += locations[i][2]
        if total_population >= 1000000:
            return distances[i]

    return -1

# Read input
n, s = map(int, input().split())
locations = []
for _ in range(n):
    x, y, k = map(int, input().split())
    locations.append((x, y, k))

# Call the function and print the output
result = is_megacity_possible(n, s, locations)
print("{:.7f}".format(result))
