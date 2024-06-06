
from collections import defaultdict
import sys

def dfs(node, parent, xor_sum):
    global boring_pairs
    for child in graph[node]:
        if child != parent:
            dfs(child, node, xor_sum ^ path_values[node][child])
    boring_pairs += xor_sum == 0

def main():
    global boring_pairs, path_values, graph
    n = int(sys.stdin.readline())
    path_values = defaultdict(dict)
    graph = defaultdict(list)
    for _ in range(n - 1):
        a, b, z = map(int, sys.stdin.readline().split())
        path_values[a][b] = z
        path_values[b][a] = z
        graph[a].append(b)
        graph[b].append(a)
    path_order = map(int, sys.stdin.readline().split())
    boring_pairs = 0
    dfs(1, -1, 0)
    print(boring_pairs)
    for path in path_order:
        a, b = graph[path]
        del path_values[a][b]
        del path_values[b][a]
        graph[a].remove(b)
        graph[b].remove(a)
        boring_pairs = 0
        dfs(1, -1, 0)
        print(boring_pairs)

if __name__ == '__main__':
    main()
