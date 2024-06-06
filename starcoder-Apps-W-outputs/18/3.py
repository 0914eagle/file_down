
from collections import deque
n=int(input())
start=[[] for i in range(n+1)]
end=[[] for i in range(n+1)]
for i in range(1,n+1):
    start[i]=list(map(int,input().split()))
for i in range(1,n+1):
    end[i]=list(map(int,input().split()))

def bfs(x,y):
    queue=deque([(x,y)])
    visited=[[0]*(n+1) for i in range(n+1)]
    while queue:
        now=queue.popleft()
        if now[0]==n and now[1]==n:
            return True
        for i in range(1,5):
            next=(now[0],now[1]+1) if i==1 else (now[0]+1,now[1]) if i==2 else (now[0],now[1]-1) if i==3 else (now[0]-1,now[1])
            if start[now[0]][now[1]-1]==0:
                continue
            if next[0]<1 or next[0]>n or next[1]<1 or next[1]>n:
                continue
            if visited[next[0]][next[1]]==1:
                continue
            if start[next[0]][next[1]-1]!=end[next[0]][next[1]-1]:
                continue
            queue.append(next)
            visited[next[0]][next[1]]=1
    return False

if start[1][0]==0 or end[1][0]==0:
    print("Impossible")
elif bfs(1,1)==False:
    print("Impossible")
else:
    print("Yes")
