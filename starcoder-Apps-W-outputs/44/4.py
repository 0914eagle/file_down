
n,m=map(int,input().split())
f=list(map(int,input().split()))
b=list(map(int,input().split()))
if len(set(f))!=n:
	print("Ambiguity")
elif len(set(b))==1:
	print("Impossible")
else:
	for i in b:
		print(f.index(i)+1,end=" ")
