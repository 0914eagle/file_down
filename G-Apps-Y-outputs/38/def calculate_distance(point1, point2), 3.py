
import itertools
import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def average_path_length(N, towns):
    total_length = 0
    num_paths = 0

    for path in itertools.permutations(towns):
        path_length = 0
        for i in range(N - 1):
            path_length += calculate_distance(path[i], path[i + 1])
        total_length += path_length
        num_paths += 1

    average_length = total_length / num_paths
    return average_length

# Reading input
N = int(input())
towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

# Calculating and printing the average length of all paths
result = average_path_length(N, towns)
print(result)
