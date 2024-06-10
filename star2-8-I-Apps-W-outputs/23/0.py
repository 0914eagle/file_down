
import sys
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] > self.size[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
    def get_size(self, x):
        return self.size[self.find(x)]
    def get_parent(self, x):
        return self.parent[x]
def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    uf = UnionFind(n)
    for i in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        uf.union(u, v)
    parent_set = set(uf.get_parent(i) for i in range(n))
    print(len(parent_set))
if __name__ == '__main__':
    main()

