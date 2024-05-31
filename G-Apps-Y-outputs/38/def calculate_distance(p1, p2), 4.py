
import itertools
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def average_path_length(N, towns):
    total_length = 0
    permutations = itertools.permutations(towns)
    num_permutations = math.factorial(N)

    for perm in permutations:
        path_length = 0
        for i in range(N - 1):
            path_length += calculate_distance(perm[i], perm[i+1])
        total_length += path_length

    average_length = total_length / num_permutations
    return average_length

# Read input
N = int(input())
towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

# Calculate and print the average path length
result = average_path_length(N, towns)
print(result)
