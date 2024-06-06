
n,m=list(map(int,input().split()))
res=[]
for i in range(m):
    x1,y1,x2,y2=list(map(int,input().split()))
    res.append(x2-x1)
    res.append(y2-y1)
print(min(res))
