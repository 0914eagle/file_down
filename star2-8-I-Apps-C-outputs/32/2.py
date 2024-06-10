
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    flights = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
    f = int(sys.stdin.readline())
    additional_flights = [list(map(int, sys.stdin.readline().split())) for _ in range(f)]
    all_flights = flights + additional_flights
    graph = [[] for _ in range(n + 1)]
    for a, b, c in all_flights:
        graph[a].append((b, c))
        graph[b].append((a, c))
    q = [1]
    visited = [False] * (n + 1)
    dist = [sys.maxsize] * (n + 1)
    dist[1] = 0
    while q:
        current = q.pop(0)
        visited[current] = True
        for neighbor, weight in graph[current]:
            if not visited[neighbor]:
                dist[neighbor] = min(dist[neighbor], dist[current] + weight)
                q.append(neighbor)
    print(sum(dist[i] for i in range(2, n + 1)))

if __name__ == "__main__":
    main()

