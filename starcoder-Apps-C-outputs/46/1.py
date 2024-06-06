
n,l,r=map(int,input().split())
lis=[]
while n>0:
    x=n%2
    lis.append(x)
    n=n//2
lis.reverse()
j=0
ans=0
for i in range(len(lis)):
    if i>=l and i<=r:
        if lis[i]==1:
            ans+=1
print(ans)
