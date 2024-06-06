
n,k=map(int,input().split())
n%=10**9+7
print((pow(2,n,10**9+7)-1)*pow(2,k,10**9+7)%(10**9+7))
