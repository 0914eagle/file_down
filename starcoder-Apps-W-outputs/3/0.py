
n,k,q=list(map(int,input().split()))
ls=[]
for i in range(n):
	l,r=list(map(int,input().split()))
	ls.append((l,r))
count=0
ans=0
for i in range(q):
	a,b=list(map(int,input().split()))
	count=0
	for j in range(n):
		if b>=ls[j][0] and a<=ls[j][1]:
			count+=1
	if count>=k:
		ans+=1
print(ans)
