
n=list(map(int,input().split()))

if max(n)-min(n)>2:
	print("NO")
else:
	print("YES")
	if min(n)==max(n):
		print(" ".join([str(i) for i in range(min(n))]+[str(i) for i in range(max(n)+1)]))
	else:
		if max(n)==2:
			print(" ".join([str(i) for i in range(min(n))] + [str(i) for i in range(3,max(n)+1)] + [str(2),str(2),str(3)]))
		else:
			print(" ".join([str(i) for i in range(min(n))]+[str(i) for i in range(max(n)+1)]))
