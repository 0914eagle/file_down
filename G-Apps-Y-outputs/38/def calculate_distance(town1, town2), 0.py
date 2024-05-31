
import itertools
import math

def calculate_distance(town1, town2):
    return math.sqrt((town1[0] - town2[0]) ** 2 + (town1[1] - town2[1]) ** 2)

def average_path_length(N, towns):
    total_length = 0
    num_paths = math.factorial(N)

    for path in itertools.permutations(towns):
        path_length = sum(calculate_distance(path[i], path[i+1]) for i in range(N - 1))
        total_length += path_length

    return total_length / num_paths

# Read input
N = int(input())
towns = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print average path length
result = average_path_length(N, towns)
print('{:.10f}'.format(result))
