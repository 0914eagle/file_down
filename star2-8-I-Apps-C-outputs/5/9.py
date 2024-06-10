
def main():
n, d = list(map(int, input().split()))
children = [[] for _ in range(n)]
for i in range(1, n):
parent = int(input())
children[parent].append(i)

def dfs(node, marked, max_marked):
if len(marked) == 0:
marked.add(node)
max_marked[0] += 1
for child in children[node]:
dfs(child, marked, max_marked)

def dfs_mark(node, marked, dist):
if len(marked) == 0:
marked.add(node)
for child in children[node]:
dfs_mark(child, marked, dist+1)

for child in children[0]:
marked = set()
max_marked = [0]
dfs(child, marked, max_marked)
for child in children[0]:
marked = set()
dfs_mark(child, marked, 1)
if len(marked) >= d:
max_marked[0] += 1

print(max_marked[0])

main()

