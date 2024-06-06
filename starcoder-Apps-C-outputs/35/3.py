
n,m=map(int,input().split())
rec=[[0,0,0,0] for i in range(m)]
for i in range(m):
    rec[i]=list(map(int,input().split()))

res=[]
for i in range(m):
    a=rec[i]
    res.append((a[0],a[1],a[2],a[3]))
    res.append((a[0],a[3],a[2],a[3]))
    res.append((a[2],a[1],a[2],a[3]))
    res.append((a[0],a[1],a[2],a[1]))

res.sort(key=lambda x:(x[2],x[1]))

vis=[0 for i in range(4*m)]
ans=0
for i in range(len(res)):
    if not vis[i]:
        vis[i]=1
        a=res[i]
        w=a[2]-a[0]+1
        h=a[3]-a[1]+1
        ans+=min(w,h)

        for j in range(i+1,len(res)):
            if not vis[j]:
                b=res[j]
                if b[0]<=a[0] and a[0]<=b[2] and b[1]<=a[1] and a[1]<=b[3]:
                    vis[j]=1
print(ans)
