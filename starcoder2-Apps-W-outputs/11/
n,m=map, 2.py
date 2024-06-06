
n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for i in range(m):
    l.append(list(map(int,input().split())))
ans=0
for i in range(m):
    s=0
    for j in range(l[i][0]-1,l[i][1]):
        s+=a[j]
    ans=max(ans,s)
print(ans)
