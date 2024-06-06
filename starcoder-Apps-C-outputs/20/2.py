
from collections import defaultdict as dd
import sys
#string = sys.stdin.read()
#words = string.split()
words = ['A', 'ABA', 'BBB', 'ABABA', 'AAAAAB']
n = len(words)
idx = {}
for i in range(len(words)):
	x = words[i]
	idx[x] = i
d = dd(set)
for i in range(n):
	for j in range(i+1, n):
		a = words[i]
		b = words[j]
		if len(a) > len(b):
			continue
		if b.startswith(a) and b.endswith(a):
			d[i].add(j)
			d[j].add(i)

#print(d)
def get_max_path(u):
	global d, visited
	if visited[u]:
		return 0
	visited[u] = True
	ans = 0
	for v in d[u]:
		if not visited[v]:
			ans = max(ans, get_max_path(v))
	return ans + 1
visited = [False for i in range(n)]
ans = 0
for i in range(n):
	if not visited[i]:
		ans = max(ans, get_max_path(i))
print(ans)

