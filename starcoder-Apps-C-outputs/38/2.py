
n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    ans += pow(i,k,1000000007)
print(ans%1000000007)
