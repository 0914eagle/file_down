
n,l,x,y=list(map(int,input().split()))
a=list(map(int,input().split()))
b=[]
for i in range(1,n):
	b.append(a[i]-a[i-1])
c=[]
if x not in b:
	c.append(x)
if y not in b:
	c.append(y)
print(len(c))
print(*c)

