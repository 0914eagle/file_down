
from itertools import permutations

def count_permutations(n, connections):
    perm_count = [0] * (2**(n-1))
    
    for perm in permutations(range(n)):
        binary_string = ''
        for i in range(n-1):
            if connections[perm[i]][perm[i+1]] == '1':
                binary_string += '1'
            else:
                binary_string += '0'
        
        idx = 0
        for i in range(n-1):
            idx += int(binary_string[i]) * (2**i)
        
        perm_count[idx] += 1
    
    return perm_count

# Input processing
n = int(input())
connections = [input() for _ in range(n)]

# Count permutations
result = count_permutations(n, connections)

# Output
print(*result)
