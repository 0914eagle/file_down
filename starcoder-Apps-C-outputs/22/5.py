
n,m,h=map(int,input().split())

a=list(map(int,input().split()))

d={}

for i in range(m):
    u,v=map(int,input().split())
    if u in d:
        d[u].append(v)
    else:
        d[u]=[v]
    if v in d:
        d[v].append(u)
    else:
        d[v]=[u]

c=0
l=[]

for i in range(n):
    x=i+1
    if x not in d:
        c+=1
        l.append(x)

print(c)
print(*l)
