
# cook your dish here
import sys

sys.setrecursionlimit(10**9)
n=int(input())
data = []
for i in range(n):
    data.append(list(input()))

visited = []
for i in range(n):
    visited.append([False]*n)

def dfs(i,j):
    if i<0 or j<0 or i>=n or j>=n:
        return False
    if data[i][j] == "E":
        return True
    if visited[i][j]:
        return False
    visited[i][j]=True
    flag1 = dfs(i+1,j)
    flag2 = dfs(i-1,j)
    flag3 = dfs(i,j+1)
    flag4 = dfs(i,j-1)
    visited[i][j]=False
    return (flag1 or flag2 or flag3 or flag4)
    
    
out = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and not dfs(i,j):
            out.append([i+1,j+1])
            visited[i][j]=True
print(len(out))
for i in out:
    print(i[0],i[1])
