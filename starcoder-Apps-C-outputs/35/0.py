
n,m=map(int,input().split())
cnt=0
for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    cnt+=min(x2-x1+1,y2-y1+1)
print(cnt)
