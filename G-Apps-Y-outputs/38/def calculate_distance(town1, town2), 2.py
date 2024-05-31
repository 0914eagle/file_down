
import itertools
import math

def calculate_distance(town1, town2):
    x1, y1 = town1
    x2, y2 = town2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def average_path_length(N, towns):
    total_length = 0
    permutations = itertools.permutations(range(N))
    
    for perm in permutations:
        path_length = 0
        for i in range(N-1):
            path_length += calculate_distance(towns[perm[i]], towns[perm[i+1]])
        total_length += path_length
    
    return total_length / math.factorial(N)

# Read input
N = int(input())
towns = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the average length of the paths
print(average_path_length(N, towns))
