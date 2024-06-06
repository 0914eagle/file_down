
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if len(set(b))==1:
	print("Ambiguity")
else:
	if len(set(a))==len(set(b)):
		print("Possible")
		for i in range(m):
			print(a[b[i]-1],end=" ")
	else:
		print("Impossible")
