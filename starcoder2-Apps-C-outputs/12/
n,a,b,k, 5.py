
n,a,b,k=map(int,input().split())
s=input()
s=s*k
s=s[:k]
ans=0
for i in range(k):
    if s[i]=='+':
        ans+=a**(k-i-1)*b**i
    else:
        ans-=a**(k-i-1)*b**i
print(ans%(10**9+9))
