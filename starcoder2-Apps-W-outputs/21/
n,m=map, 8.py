
n,m=map(int,input().split())
l=[]
for i in range(n):
    a,s=map(int,input().split())
    l.append([a,s])
l.sort()
ans=0
for i in range(n):
    if l[i][0]>=m:
        ans+=1
    else:
        m=l[i][0]+l[i][1]
print(ans)
