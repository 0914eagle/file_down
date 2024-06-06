
'''
这个问题可以分成两个部分：
1.找出最大的独立集
2.找出最大的环
这两个问题的解法大同小异，这里只贴第一个解法的代码：
'''
import sys
from collections import defaultdict

'''
以n = 5 为例：
当n<10时，我们直接找一个最大的环
当n>=10时，我们找一个最大的独立集
'''

def find_max_independent_set(n, edges):
    graph = defaultdict(list)
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    def dfs(u, v, visited):
        visited.add(u)
        visited.add(v)
        for node in graph[u]:
            if node != v and node not in visited:
                dfs(v, node, visited)

    visited = set()
    for u, vs in graph.items():
        for v in vs:
            if u < v and u not in visited and v not in visited:
                dfs(u, v, visited)
                break
    return visited

if __name__ == "__main__":
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    edges = []
    for i in range(m):
        edges.append(list(map(int, sys.stdin.readline().strip().split())))
    print(1)
    print(len(find_max_independent_set(n, edges)), *sorted(find_max_independent_set(n, edges)))
