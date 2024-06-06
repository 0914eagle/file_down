
from collections import deque
n,k=map(int,input().split())
s=input()
d=deque()
cost=[]
for i in range(n):
	cost.append(int(input()))
ans=0
for i in range(n):
	if(s[i]=='('):
		d.append([i,1])
	else:
		if(len(d)==0):
			d.append([i,-1])
			ans+=cost[i]
		else:
			if(d[-1][1]==-1):
				d.pop()
				ans+=cost[i]
			else:
				d.append([i,-1])
				ans+=cost[i]
				if(len(d)>k):
					if(d[0][1]==1):
						d.popleft()
					else:
						ans-=cost[d[0][0]]
						d.popleft()
print(ans)
