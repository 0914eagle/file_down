
n,m=map(int,input().split())
a=list(map(int,input().split()))
w=list(map(int,input().split()))
sum=0
for i in range(n):
    sum+=w[i]
ans=[]
for i in range(n):
    if a[i]:
        ans.append((w[i]+m)*998244353//sum)
    else:
        ans.append((w[i]-m)*998244353//sum)
for i in range(n):
    print(ans[i])

