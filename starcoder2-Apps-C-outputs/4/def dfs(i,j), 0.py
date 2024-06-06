
def dfs(i,j):
    if i==n:
        if j in s:
            return 0
        else:
            s.add(j)
            return 1
    if j in s:
        return dfs(i+1,j)
    else:
        s.add(j)
        return dfs(i+1,j)+dfs(i+1,j+1)
n=int(input())
v=list(map(int,input().split()))
s=set()
print(dfs(1,v[0]))
