
n = int(input())
maxx = -1
maxn = -1
for i in range(n):
	l,r = map(int,input().split())
	if l>maxx:
		maxx = l+r
		maxn = r
	else:
		maxx = maxx+r
		maxn = max(maxn,r)
print(maxx,maxn)
