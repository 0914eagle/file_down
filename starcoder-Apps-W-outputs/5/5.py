
def dfs(graph,s,visited,stack):
    visited[s]=True
    for i in graph[s]:
        if visited[i]==False:
            dfs(graph,i,visited,stack)
    stack.append(s)
    
def dfs2(graph,s,visited):
    visited[s]=True
    for i in graph[s]:
        if visited[i]==False:
            dfs2(graph,i,visited)
    
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
graph_rev=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph_rev[b].append(a)
visited=[False]*(n+1)
stack=[]
for i in range(1,n+1):
    if visited[i]==False:
        dfs(graph,i,visited,stack)
visited=[False]*(n+1)
count=0
for i in stack[::-1]:
    if visited[i]==False:
        dfs2(graph_rev,i,visited)
        count+=1
if count==1:
    print("Connected")
else:
    for i in range(1,n+1):
        if visited[i]==False:
            print(i)
