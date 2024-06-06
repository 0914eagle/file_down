
n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[]
r=[]
for i in range(m):
    l1,r1=map(int,input().split())
    l.append(l1)
    r.append(r1)
ans=0
for i in range(m):
    for j in range(i+1,m):
        if l[i]<=l[j] and r[j]<=r[i]:
            ans=max(ans,sum(a[l[i]-1:r[i]]))
        elif l[j]<=l[i] and r[i]<=r[j]:
            ans=max(ans,sum(a[l[j]-1:r[j]]))
        elif l[i]<=l[j] and r[j]<=r[i]:
            ans=max(ans,sum(a[l[j]-1:r[i]]))
        elif l[j]<=l[i] and r[i]<=r[j]:
            ans=max(ans,sum(a[l[i]-1:r[j]]))
print(ans)
