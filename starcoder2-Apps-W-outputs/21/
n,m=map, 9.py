
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort()
ans=0
for i in range(n):
    if a[i][0]>=m:
        ans+=1
    else:
        a[i][0]=0
a.sort(key=lambda x:x[1])
for i in range(n):
    if a[i][0]>=m:
        ans+=1
    else:
        a[i][0]=0
print(ans)
