
import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    n = int(sys.stdin.readline())
    
    uf = UnionFind(26)
    
    for _ in range(n):
        s = sys.stdin.readline().split()
        
        if s[1] == "is":
            uf.union(ord(s[0][0]) - ord("a"), ord(s[2][0]) - ord("a"))
        else:
            if uf.same(ord(s[0][0]) - ord("a"), ord(s[2][0]) - ord("a")):
                print("wait what?")
                return
    
    print("yes")
    
main()

