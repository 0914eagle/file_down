
import itertools
import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def average_path_length(N, towns):
    paths = list(itertools.permutations(towns))
    total_length = 0

    for path in paths:
        length = 0
        for i in range(N - 1):
            length += calculate_distance(path[i], path[i + 1])
        total_length += length

    average_length = total_length / math.factorial(N)
    return average_length

# Input processing
N = int(input())
towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

# Calculate and print the average length of paths
print(average_path_length(N, towns))
