
from collections import defaultdict
def solve(n, m, h, u, clients):
    client_centers = defaultdict(list)
    for i, (c1, c2) in enumerate(clients):
        client_centers[c1].append(i)
        client_centers[c2].append(i)
    
    centers = set()
    for c, client_list in client_centers.items():
        for client in client_list:
            c1, c2 = clients[client]
            if u[c1] == u[c2]:
                centers.add(c)
    
    return len(centers), centers

n, m, h = map(int, input().split())
u = list(map(int, input().split()))
clients = [tuple(map(int, input().split())) for _ in range(m)]
k, centers = solve(n, m, h, u, clients)
print(k)
print(*sorted(centers))

