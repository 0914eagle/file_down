
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort()
ans=0
b=[0]*n
for i in range(n):
    b[i]=a[i][0]+a[i][1]
for i in range(n):
    if b[i]-a[i][0]<=m:
        ans+=1
    else:
        break
print(ans)
