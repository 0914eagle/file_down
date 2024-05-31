
def count_permutations(n, connections):
    memo = {}
    for i in range(1 << (n-1)):
        s = bin(i)[2:].zfill(n-1)
        memo[s] = 0
    
    for perm in itertools.permutations(range(n)):
        s = ''
        for i in range(n-1):
            s += '1' if connections[perm[i]][perm[i+1]] == '1' else '0'
        
        memo[s] += 1
    
    result = []
    for i in range(1 << (n-1)):
        s = bin(i)[2:].zfill(n-1)
        result.append(memo[s])
    
    return result

import itertools
n = int(input())
connections = [input() for _ in range(n)]
result = count_permutations(n, connections)
print(*result)
