
n,x,k=map(int,input().split())
s=input().split()
l=0
r=0
c=0
while l<n:
    while r<n and c<k:
        if int(s[r])%x==0:
            c+=1
        r+=1
    if c==k:
        ans+=(n-r)
    r+=1
    l+=1
print(ans)
