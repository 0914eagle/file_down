
import itertools
import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def average_path_length(N, towns):
    total_length = 0
    num_paths = 0

    for perm in itertools.permutations(towns):
        path_length = 0
        for i in range(N-1):
            path_length += calculate_distance(perm[i], perm[i+1])
        total_length += path_length
        num_paths += 1

    return total_length / num_paths

# Read input
N = int(input())
towns = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print average path length
result = average_path_length(N, towns)
print(result)
