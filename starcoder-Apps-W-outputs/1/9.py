
'''
code by : Boss
'''
import sys,math
from collections import deque,defaultdict

input = sys.stdin.readline

def get_ints():
    return map(int, input().strip().split())

def get_array():
    return list(map(int, input().strip().split()))

def printlist(a) : 
    return ' '.join(list(map(str, a)))

n,m = get_ints()
g = defaultdict(set)
for _ in range(m):
    u,v = get_ints()
    g[u].add(v)
    g[v].add(u)

visited = set()
ok = True
for i in range(1,n+1):
    if i not in visited:
        q = deque([i])
        visited.add(i)
        while q:
            cur = q.popleft()
            for j in g[cur]:
                if j not in visited:
                    visited.add(j)
                    q.append(j)
        if len(visited) == n:
            ok = False

if ok:
    print("Yes")
else:
    print("No")
