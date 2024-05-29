
from itertools import permutations

def shortest_good_subsequence(n, graph, m, path):
    shortest_subsequence = []
    shortest_length = float('inf')

    for perm in permutations(path[1:-1]):
        perm = (path[0],) + perm + (path[-1],)
        length = 0
        
        for i in range(len(perm) - 1):
            length += 1 - int(graph[perm[i] - 1][perm[i + 1] - 1])

        if length < shortest_length:
            shortest_length = length
            shortest_subsequence = perm

    return shortest_length, shortest_subsequence

# Read input
n = int(input())
graph = [input() for _ in range(n)]
m = int(input())
path = list(map(int, input().split()))

# Call the function and print the output
k, v = shortest_good_subsequence(n, graph, m, path)
print(k)
print(*v)
