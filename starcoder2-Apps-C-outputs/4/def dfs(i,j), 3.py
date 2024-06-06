
def dfs(i,j):
    global ans
    if j in vis:
        return
    vis.add(j)
    if i==n:
        ans+=1
        return
    for k in range(n):
        if k not in vis and (k==0 or j+1==a[k]):
            dfs(i+1,a[k])
n=int(input())
a=list(map(int,input().split()))
ans=0
vis=set()
dfs(0,a[0])
print(ans)
