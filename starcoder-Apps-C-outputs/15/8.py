
n,c=map(int,input().split())
p=1000000007
f=[1,1]
for i in range(2,n+1):
	f.append(f[-1]*i%p)
print(f[n]*pow(f[c]*f[n-c-1],p-2,p)%p)
