
n,m=map(int,input().split())
if n==1:
    print(m)
else:
    print((m**n+m-1)%(10**9+7))
