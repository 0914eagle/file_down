
def dfs(x,y):
	if x==n:
		return True
	for i in range(4):
		if v[x][i]==0:
			continue
		if w[y][i]==0:
			continue
		if (i==0 and w[y][1]!=0) or (i==1 and w[y][2]!=0) or (i==2 and w[y][3]!=0) or (i==3 and w[y][0]!=0):
			continue
		if v[x][i]!=w[y][i]:
			continue
		if v[x][i]==w[y][i]:
			if dfs(x+1,v[x][i]):
				return True
	return False
n=int(input())
v=[]
for i in range(n):
	v.append(list(map(int,input().split())))
w=[]
for i in range(n):
	w.append(list(map(int,input().split())))
if dfs(1,1):
	print("Yes")
else:
	print("No")
