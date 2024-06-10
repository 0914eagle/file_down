
n,k=map(int,input().split())
h=list(map(int,input().split()))

ans=0
for a in range(1,k+1):
    cur=0
    for i in range(n):
        if a==h[i]:
            cur+=1
        if a==h[(i+1)%n]:
            cur+=1
        if cur>1:
            ans+=1
            break

print(ans%998244353)

