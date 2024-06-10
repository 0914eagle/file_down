
import sys
from heapq import heappush, heappop

def main():
    n, r = map(int, input().split())
    flights = []
    for _ in range(r):
        a, b, c = map(int, input().split())
        flights.append((a, b, c))
    
    f = int(input())
    for _ in range(f):
        a, b, c = map(int, input().split())
        flights.append((a, b, c))
    
    dist = [sys.maxsize] * (n + 1)
    dist[1] = 0
    pq = []
    for a, b, c in flights:
        if dist[a] + c < dist[b]:
            dist[b] = dist[a] + c
            heappush(pq, (dist[b], b))
    
    while pq:
        cost, city = heappop(pq)
        if cost > dist[city]:
            continue
        for a, b, c in flights:
            if a == city:
                if dist[a] + c < dist[b]:
                    dist[b] = dist[a] + c
                    heappush(pq, (dist[b], b))
    
    print(dist[1])

if __name__ == "__main__":
    main()

