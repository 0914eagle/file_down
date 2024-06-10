
n,l=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
d=[]
for i in range(n):
    d.append([c[i]/a[i],i])
d.sort()
e=f=0
for i in range(n):
    if i<l:
        e+=a[d[i][1]]
    else:
        f+=a[d[i][1]]
print((c[d[l-1][1]]/e)*(c[d[n-1][1]]/f))

