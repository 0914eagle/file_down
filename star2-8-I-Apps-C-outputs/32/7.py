
import sys

def main():
    n, r = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(r):
        a, b, c = map(int, input().split())
        adj[a-1].append((b-1, c*2))
        adj[b-1].append((a-1, c*2))
    
    f = int(input())
    for _ in range(f):
        a, b, c = map(int, input().split())
        adj[a-1].append((b-1, c))
        adj[b-1].append((a-1, c))
    
    dist = [sys.maxsize] * n
    dist[0] = 0
    
    pq = [(0, 0)]
    while pq:
        c, v = pq.pop(0)
        
        for u, w in adj[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                pq.append((dist[u], u))
    
    print(dist[0])

if __name__ == '__main__':
    main()

