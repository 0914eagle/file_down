
n,m=map(int,input().split())
p=list(map(int,input().split()))
l=[]
for i in range(m):
    a,b=map(int,input().split())
    l.append((a,b))
d={}
for i in range(n):
    d[p[i]]=i
def swap(a,b):
    x,y=d[a],d[b]
    d[a],d[b]=d[b],d[a]
    p[x],p[y]=p[y],p[x]
for a,b in l:
    swap(a,b)
print(*p)

