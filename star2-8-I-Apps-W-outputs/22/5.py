
n = int(input())
a = list(map(int, input().split()))

from collections import defaultdict
adj = defaultdict(list)
for i, val in enumerate(a):
    adj[i+1].append(val)
    
def dfs(node, parent):
    for neigh in adj[node]:
        if neigh != parent:
            dfs(neigh, node)

def solve(node, parent):
    for neigh in adj[node]:
        if neigh != parent:
            dfs(neigh, node)
            
def solve_tree():
    for i in range(1, n+1):
        if len(adj[i]) > 1:
            solve(i, -1)
            break
            
solve_tree()

print((1 << n) - 2 % (10**9 + 7))

