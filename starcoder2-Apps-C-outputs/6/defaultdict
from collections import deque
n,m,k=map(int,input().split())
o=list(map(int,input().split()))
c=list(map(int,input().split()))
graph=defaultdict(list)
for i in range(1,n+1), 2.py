
from collections import defaultdict
from collections import deque
n,m,k=map(int,input().split())
o=list(map(int,input().split()))
c=list(map(int,input().split()))
graph=defaultdict(list)
for i in range(1,n+1):
    a=list(map(int,input().split()))
    for j in range(1,a[0]+1):
        graph[i].append(a[j])

def bfs(s,e):
    q=deque()
    q.append(s)
    visited=[False]*(n+1)
    visited[s]=True
    while q:
        s=q.popleft()
        if s==e:
            return True
        for i in graph[s]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
    return False

for i in o:
    if bfs(1,i):
        for j in c:
            if bfs(i,j):
                print(2)
                exit()
print("impossible")
