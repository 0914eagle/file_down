
from collections import defaultdict
from sys import stdin, stdout
 
def find_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]
 
def union(parent, rank, x, y):
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1
 
def find_max_hive(n, edges):
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    for u, v in edges:
        union(parent, rank, u, v)
    for i in range(n):
        parent[i] = find_parent(parent, i)
    num_hive = len(set(parent))
    return num_hive
 
def main():
    n, m = map(int, stdin.readline().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, stdin.readline().strip().split())
        edges.append((u, v))
    num_hive = find_max_hive(n, edges)
    stdout.write(str(num_hive) + '\n')
 
if __name__ == '__main__':
    main()

