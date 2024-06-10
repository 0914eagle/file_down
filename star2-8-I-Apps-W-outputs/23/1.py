
from sys import stdin, stdout
from collections import defaultdict

def find_parent(tree, parent):
	if parent[tree] == tree:
		return tree
	parent[tree] = find_parent(parent[tree], parent)
	return parent[tree]

def union(tree1, tree2, parent, rank):
	root1 = find_parent(tree1, parent)
	root2 = find_parent(tree2, parent)
	if rank[root1] < rank[root2]:
		parent[root1] = root2
	elif rank[root1] > rank[root2]:
		parent[root2] = root1
	else:
		parent[root2] = root1
		rank[root1] += 1

def kruskal(graph):
	parent = {}
	rank = {}
	for tree in graph:
		parent[tree] = tree
		rank[tree] = 0
	mst = []
	edges = []
	for u, v in graph:
		edges.append((u, v))
	edges = sorted(edges, key=lambda x: x[2])
	for u, v, w in edges:
		if find_parent(u, parent) != find_parent(v, parent):
			union(u, v, parent, rank)
			mst.append((u, v, w))
	return mst

def main():
	n, m = map(int, stdin.readline().split())
	graph = defaultdict(list)
	for _ in range(m):
		u, v = map(int, stdin.readline().split())
		graph[u].append(v)
		graph[v].append(u)
	mst = kruskal(graph)
	if len(mst) == n - 1:
		stdout.write(str(n))
	else:
		stdout.write('impossible')

main()

