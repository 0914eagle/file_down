
def redirect_roads(N, E, roads):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    for a, b in roads:
        adj_list[a].append(b)

    in_degrees = [0] * (N+1)
    out_degrees = [0] * (N+1)
    for a, b in roads:
        out_degrees[a] += 1
        in_degrees[b] += 1

    if not all(in_degrees[i] == out_degrees[i] for i in range(1, N+1)):
        print("NO")
        return

    print("YES")
    for a, b in roads:
        print(a, b)

# Example usage
N, E = 3, 3
roads = [(1, 2), (2, 3), (3, 1)]
redirect_roads(N, E, roads)
```
