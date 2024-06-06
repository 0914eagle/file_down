
from collections import defaultdict
from sys import stdin, stdout

def dfs(node, parent, visited, jokes):
    visited[node] = True
    jokes[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child, node, visited, jokes)
            jokes[node] |= jokes[child]
    if parent != -1:
        jokes[parent] |= jokes[node]

def solve(node, parent, visited, jokes):
    visited[node] = True
    if parent != -1:
        jokes[node] |= jokes[parent]
    if node == 1:
        return 1
    ans = 0
    for child in graph[node]:
        if not visited[child]:
            ans += solve(child, node, visited, jokes)
    if jokes[node]:
        ans += 1
    return ans

def main():
    n = int(stdin.readline())
    jokes = defaultdict(bool)
    graph = defaultdict(list)
    for i in range(1, n):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for i, v in enumerate(map(int, stdin.readline().split())):
        jokes[i + 1] = v
    visited = [False] * (n + 1)
    dfs(1, -1, visited, jokes)
    visited = [False] * (n + 1)
    stdout.write(str(solve(1, -1, visited, jokes)))

main()
