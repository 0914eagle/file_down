
import itertools
import math

def calculate_distance(town1, town2):
    return math.sqrt((town1[0] - town2[0]) ** 2 + (town1[1] - town2[1]) ** 2)

def average_length_of_paths(N, towns):
    total_length = 0
    num_paths = 0
    
    for path in itertools.permutations(towns):
        path_length = 0
        for i in range(N - 1):
            path_length += calculate_distance(path[i], path[i+1])
        total_length += path_length
        num_paths += 1
    
    return total_length / num_paths

# Read input
N = int(input())
towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

average_length = average_length_of_paths(N, towns)
print(average_length)
