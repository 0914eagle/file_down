
from collections import defaultdict
from sys import setrecursionlimit


def dfs(node, group):
    connected_groups.add(group)
    for adj in graph[node]:
        if adj not in visited:
            visited.add(adj)
            dfs(adj, group)


def solve(n, a):
    graph = defaultdict(list)
    for i in range(n-1):
        graph[i+1].append(i+2)
        graph[i+2].append(i+1)

    for i in range(n):
        graph[a[i]].append(i+1)
        graph[i+1].append(a[i])

    visited = set()
    connected_groups = set()
    for i in range(1, n+1):
        if i not in visited:
            visited.add(i)
            dfs(i, a[i-1])
    
    return len(connected_groups) == n


if __name__ == '__main__':
    setrecursionlimit(10**6)
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if solve(n, a):
            print("YES")
            for i in range(n-1):
                print(f"{i+1} {i+2}")
        else:
            print("NO")

