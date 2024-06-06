
# Source: https://open.kattis.com/problems/city

from sys import stdin
from math import inf

def find_min_distance(coordinates, max_distance):
    

    # Sort the coordinates by x-coordinate
    coordinates.sort(key=lambda coord: coord[0])

    # Initialize variables for the minimum distance and the coordinates of the intersection
    min_distance = inf
    intersection_x = 0

    # Find the intersection point
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]

        if abs(x1 - x2) <= max_distance:
            intersection_x = (x1 + x2) / 2
            break

    if intersection_x == 0:
        return 'impossible'

    # Find the minimum distance to travel for each citizen
    for x, y in coordinates:
        min_distance = min(min_distance, abs(x - intersection_x) + abs(y - y))

    return min_distance


# Read the input
n = int(stdin.readline())
coordinates = []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    coordinates.append((x, y))
max_distance = int(stdin.readline())

# Find the minimum distance to travel for the citizens
min_distance = find_min_distance(coordinates, max_distance)

# Print the minimum distance
print(min_distance)
