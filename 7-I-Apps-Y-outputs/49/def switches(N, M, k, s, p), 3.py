
from itertools import combinations

def switches(N, M, k, s, p):
    # Write your code here
    result = 0
    for i in range(M):
        switches = []
        for j in range(k[i]):
            switches.append(s[i][j])
        for comb in combinations(switches, p[i]):
            result += 1
    return result

