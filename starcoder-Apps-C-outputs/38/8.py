
n,k=map(int,input().split())
ans=0
for i in range(n,0,-1):
  ans+=i**k
print(ans%(1000000007))
