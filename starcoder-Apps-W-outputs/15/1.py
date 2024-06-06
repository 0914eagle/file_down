
def dfs(s,t):
    s=int(s)-1
    t=int(t)-1
    for i in range(n):
        if s in G[i]:
            if i==t:
                return 'YES'
            else:
                G[i].remove(s)
                ans=dfs(i+1,t)
                G[i].add(s)
                if ans=='YES':
                    return 'YES'
    return 'NO'
n=int(input())
G=[set() for i in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    for j in range(i):
        if G[j] and a<max(G[j]) and b>min(G[j]):
            G[i].add(j)
            G[j].add(i)
print(dfs(*input().split()))
