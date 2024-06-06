
n,m=map(int,input().split())
s=list(map(int,input().split()))
m=m*m
ans=0
for i in range(n):
    if s[i]>m:
        ans+=0
    else:
        if s[i]==1:
            ans+=m
        else:
            ans+=(s[i]-1)*2
print(ans)
