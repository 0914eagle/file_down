
n, m = map(int, input().split())

s = list(map(int, input().split()))

d = []

g = []

for i in range(m):
	t = list(map(int, input().split()))
	d.append(t[0])
	g.append(t[1])

for i in range(n):
	ans = 0
	for j in range(m):
		if s[i] >= d[j]:
			ans = ans + g[j]
	print(ans, end = " ")
