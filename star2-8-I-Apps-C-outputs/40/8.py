
from collections import defaultdict
from heapq import heappush, heappop

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.dist = float("inf")
        self.adj = defaultdict(int)
        
    def __lt__(self, other):
        return self.dist < other.dist
        
    def __repr__(self):
        return f"Node {self.idx} with dist {self.dist}"
    
class Graph:
    def __init__(self, n):
        self.nodes = [Node(i) for i in range(n)]
        
    def add_edge(self, u, v, c):
        self.nodes[u].adj[v] = c
        
    def dijkstra(self, src):
        self.nodes[src].dist = 0
        
        pq = []
        for node in self.nodes:
            heappush(pq, node)
            
        while pq:
            curr = heappop(pq)
            
            for adj_idx, c in curr.adj.items():
                adj = self.nodes[adj_idx]
                if adj.dist > curr.dist + c:
                    adj.dist = curr.dist + c
                    heappush(pq, adj)
                    
    def get_dist(self, idx):
        return self.nodes[idx].dist

def main():
    n, m, alpha = map(int, input().split())
    
    g = Graph(n)
    
    for _ in range(m):
        u, v, c = map(int, input().split())
        g.add_edge(u-1, v-1, c)
        
    g.dijkstra(0)
    
    max_candies = max(g.get_dist(i) for i in range(n))
    
    if max_candies == float("inf"):
        print("Poor girl")
    else:
        print(max_candies**2 + alpha * m)
        
if __name__ == "__main__":
    main()

