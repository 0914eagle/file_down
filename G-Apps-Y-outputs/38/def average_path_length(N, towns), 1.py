
import itertools
import math

def average_path_length(N, towns):
    total_length = 0
    num_paths = math.factorial(N)
    
    for path in itertools.permutations(range(N)):
        length = 0
        for i in range(N-1):
            x1, y1 = towns[path[i]]
            x2, y2 = towns[path[i+1]]
            length += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        total_length += length
    
    return total_length / num_paths

# Input
N = int(input())
towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

# Output
result = average_path_length(N, towns)
print(result)
