
n,m=map(int,input().split())
a=[0]*m
for i in range(n):
    s=list(input())
    for j in range(m):
        if s[j]=='A':a[j]+=1
        elif s[j]=='B':a[j]+=2
        elif s[j]=='C':a[j]+=3
        elif s[j]=='D':a[j]+=4
        elif s[j]=='E':a[j]+=5
c=list(map(int,input().split()))
ans=0
for i in range(m):
    ans+=a[i]*c[i]
print(ans)
