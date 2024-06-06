
n,k=map(int,input().split())
x=list(map(int,input().split()))
z=list(map(int,input().split()))

for i in range(1,n):
	x[i]+=x[i-1]
	z[i]+=z[i-1]

if k&1:
	print(min(x[n-1],z[n-1]))
else:
	print(min(x[n-1]-min(x[n-2],z[n-2]),z[n-1]-min(x[n-2],z[n-2])))
