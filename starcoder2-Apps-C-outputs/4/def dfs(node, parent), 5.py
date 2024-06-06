
import sys
sys.setrecursionlimit(10**9)

def dfs(node, parent):
    global ans
    if node not in visited:
        visited.add(node)
        if node in jokes:
            jokes[node].add(jokes[parent])
        else:
            jokes[node] = set([jokes[parent]])
        dfs(parent, node)
    else:
        if node in jokes:
            if jokes[node] == jokes[parent]:
                ans += 1
            else:
                ans = 0
                return

n = int(input())
jokes = {1: 0}
for i in range(1, n):
    jokes[i+1] = int(input())

for i in range(n-1):
    a, b = map(int, input().split())
    if a not in jokes:
        jokes[a] = set([jokes[b]])
    else:
        jokes[a].add(jokes[b])

ans = 0
visited = set()
for i in range(2, n+1):
    dfs(i, i-1)

print(ans)
