
n,m=map(int,input().split())
a=list(map(int,input().split()))
w=list(map(int,input().split()))
MOD=998244353
f=[0]*n
for i in range(n):
    if a[i]:
        f[i]+=m+1
    else:
        f[i]-=1
for i in range(n):
    print((f[i]*pow(w[i],MOD-2,MOD))%MOD)

