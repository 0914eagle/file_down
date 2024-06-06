
n,a,b,k=map(int,input().split())
s=input()
ans=0
for i in range(k):
    ans+=(-1)**(i)*(a**(n-i))*(b**i)
print(ans%(10**9+9))
