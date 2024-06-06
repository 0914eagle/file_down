
n,m=map(int,input().split())
s=[]
for i in range(m):
    l,r,y=map(int,input().split())
    s.append((l,-1,y))
    s.append((r,1,y))
s.sort()
cnt,ans=0,[]
for l,t,y in s:
    if t==-1:
        if cnt==n:
            print("impossible")
            exit(0)
        cnt+=1
    else:
        cnt-=1
    ans.append(y)
print("".join(ans))
