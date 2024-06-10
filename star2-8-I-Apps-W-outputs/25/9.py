
class DisjointSet:
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
    
def solve(n, m, k, buildings):
    disjoint_set = DisjointSet(m)
    
    for b in buildings:
        disjoint_set.union(b - 1, b)
    
    counts = [0] * m
    
    for b in buildings:
        counts[disjoint_set.find(b - 1)] += 1
    
    counts.sort(reverse=True)
    
    empty = 0
    total_noise = 0
    
    for count in counts:
        if empty < k:
            total_noise += count
            empty += 1
        else:
            total_noise += count - 1
    
    return total_noise

