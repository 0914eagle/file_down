
from collections import deque
n=int(input())
node=[]
for i in range(n):
    a,b=map(int,input().split())
    node.append([a,b])
node.sort(key=lambda x:x[0],reverse=True)
check=[0]*n
answer=0
for i in range(n):
    if node[i][1]==0:
        answer+=1
        check[i]=1
        queue=deque([node[i][0]])
        while queue:
            x=queue.popleft()
            for j in range(n):
                if node[j][1]==x and check[j]==0:
                    queue.append(node[j][0])
                    check[j]=1
print(answer)
