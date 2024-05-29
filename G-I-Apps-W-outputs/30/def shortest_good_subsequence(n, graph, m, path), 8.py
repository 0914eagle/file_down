
from itertools import combinations

def shortest_good_subsequence(n, graph, m, path):
    def bfs(start, end):
        queue = [(start, [start])]
        while queue:
            current, path = queue.pop(0)
            if current == end:
                return path
            for i in range(n):
                if graph[current][i] == 1 and i not in path:
                    queue.append((i, path + [i]))

    good_subsequences = []
    for i in range(2, m + 1):
        for subseq in combinations(path[1:-1], i - 2):
            subseq = [path[0]] + list(subseq) + [path[-1]]
            valid = True
            for j in range(len(subseq) - 1):
                if not bfs(subseq[j], subseq[j+1]):
                    valid = False
                    break
            if valid:
                good_subsequences.append(subseq)

    shortest_subseq = min(good_subsequences, key=len)
    return len(shortest_subseq), shortest_subseq

# Input parsing
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
m = int(input())
path = list(map(int, input().strip().split()))

# Call the function and print the output
k, result = shortest_good_subsequence(n, graph, m, path)
print(k)
print(' '.join(map(str, result)))
