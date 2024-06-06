
a,b,n,m=map(int,input().split())
s1=[]
s2=[]
for i in range(n+m):
    if i<n:
        x,y=map(int,input().split())
        s1.append((x,y))
    else:
        x,y=map(int,input().split())
        s2.append((x,y))
s1.sort(key=lambda x:x[0])
s1.sort(key=lambda x:x[1])
ans=n
for i in s1:
    for j in s2:
        if i[0]+15<j[0] and i[1]+9<j[1] and j[0]-i[0]-15>=0 and j[1]-i[1]-9>=0:
            ans-=1
            break
print(ans)
