
class union_find(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        if self.rank[x] >= self.rank[y]:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        else:
            self.parent[x] = y

if __name__ == '__main__':
    n = int(input())
    uf = union_find(n + 1)
    while n > 0:
        n -= 1
        q, a, b = map(int, input().split())
        if q == 1:
            uf.union(a, b)
        else:
            if uf.find(a) == uf.find(b):
                print("YES")
            else:
                print("NO")
