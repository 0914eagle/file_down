
# 并查集
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    u, v = map(int, input().split())
    uf.union(u - 1, v - 1)

cnt = 0
for i in range(n):
    if uf.parent[i] == i:
        cnt += 1

print(cnt - 1)
for i in range(1, n):
    print(uf.find(i) + 1)
