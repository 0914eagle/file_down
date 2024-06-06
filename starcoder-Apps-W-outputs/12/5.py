
n,t,c=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
ans=0
for i in a:
    if(i<=t):
        cnt+=1
    else:
        cnt=0
    if(cnt==c):
        ans+=1
        cnt-=1
print(ans)
