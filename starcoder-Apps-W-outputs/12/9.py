
n,t,c=map(int,input().split())
a=list(map(int,input().split()))
count=0
current=0
for i in a:
	if i<=t:
		count+=1
	else:
		current+=1
		count-=current
		if count<0:
			count=0
print(count)
