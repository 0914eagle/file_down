
from itertools import permutations

def shortest_good_subsequence(n, graph, m, path):
    def is_valid_path(seq):
        for i in range(len(seq) - 1):
            if not graph[seq[i]][seq[i+1]]:
                return False
        return True

    def shortest_path_length(seq):
        length = 0
        for i in range(len(seq) - 1):
            length += 1
        return length

    shortest_subsequence = None
    shortest_length = float('inf')

    for k in range(2, m):
        for subsequence in permutations(path, k):
            if subsequence[0] == path[0] and subsequence[-1] == path[-1]:
                if is_valid_path(subsequence):
                    length = shortest_path_length(subsequence)
                    if length < shortest_length:
                        shortest_length = length
                        shortest_subsequence = subsequence

    return shortest_length, shortest_subsequence

# Input
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

m = int(input())
path = list(map(int, input().strip().split()))

# Output
length, subsequence = shortest_good_subsequence(n, graph, m, path)
print(length)
print(' '.join(map(str, subsequence)))
