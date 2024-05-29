
from itertools import permutations

def find_shortest_good_subsequence(n, graph, m, path):
    shortest_good_subsequence = None
    shortest_length = float('inf')
    
    for k in range(2, m+1):
        for perm in permutations(path, k):
            perm = list(perm)
            perm.insert(0, perm[0])
            perm.append(perm[-1])
            is_good = True
            for i in range(1, k):
                if not graph[perm[i-1]-1][perm[i]-1]:
                    is_good = False
                    break
            if is_good:
                if k < shortest_length:
                    shortest_length = k
                    shortest_good_subsequence = perm[1:-1]
    
    return shortest_length, shortest_good_subsequence

# Reading input
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
m = int(input())
path = list(map(int, input().split()))

# Finding the shortest good subsequence
length, result = find_shortest_good_subsequence(n, graph, m, path)

# Output
print(length)
print(' '.join(map(str, result)))
