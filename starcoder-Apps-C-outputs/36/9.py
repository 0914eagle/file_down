
n,m=map(int,input().split())
a=list(map(int,input().split()))
s=[]
f=[]
for i in range(m):
	d=list(map(int,input().split()))
	s.append(d[0])
	f.append(d[1:])
ans=0
for i in range(m):
	c=0
	for j in f[i]:
		c=c^a[j-1]
	if s[i]==c:
		ans+=1
if ans==m:
	print('YES')
else:
	print('NO')

