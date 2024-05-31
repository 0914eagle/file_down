
import itertools
import math

def average_path_length(N, towns):
    total_length = 0
    total_permutations = math.factorial(N)
    
    for perm in itertools.permutations(range(N)):
        path_length = 0
        for i in range(N-1):
            x1, y1 = towns[perm[i]]
            x2, y2 = towns[perm[i+1]]
            path_length += math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
        total_length += path_length
    
    average_length = total_length / total_permutations
    return average_length

# Read input
N = int(input())
towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

# Calculate and print average path length
result = average_path_length(N, towns)
print(result)
