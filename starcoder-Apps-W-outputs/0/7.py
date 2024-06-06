

import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)


def dfs(graph, v, used, ans):
    used[v] = 1
    for to in graph[v]:
        if not used[to]:
            dfs(graph, to, used, ans)
    ans.append(v)


def topsort(graph, used, ans):
    for i in range(len(graph)):
        if not used[i]:
            dfs(graph, i, used, ans)
    ans.reverse()


def main():
    # read the list of dependencies and build a graph of tasks
    n, m = map(int, input().split())
    es = list(map(int, input().split()))
    graph = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].add(a)
    # get the topological sort of the tasks graph
    used = [0] * n
    ans = []
    topsort(graph, used, ans)
    # find the number of coprocessor calls
    res = 0
    c = es[ans[0]]
    for v in ans:
        if es[v] != c:
            res += 1
            c = es[v]
    print(res)


if __name__ == '__main__':
    main()

