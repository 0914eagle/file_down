
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort()
ans=0
for i in range(n):
    if a[i][0]>ans:
        ans=a[i][0]
    ans+=a[i][1]
print(ans)
