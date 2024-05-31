
import itertools
import math

def average_path_length(N, towns):
    total_length = 0
    num_paths = 0
    
    for perm in itertools.permutations(towns):
        path_length = 0
        for i in range(N-1):
            x1, y1 = perm[i]
            x2, y2 = perm[i+1]
            path_length += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        total_length += path_length
        num_paths += 1
    
    return total_length / num_paths

# Input processing
N = int(input())
towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

# Calculate and print the average length of the paths
print('{:.10f}'.format(average_path_length(N, towns)))
