
def is_k_multihedgehog(n, k, edges):
    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    center_degree = 0
    for degree in degrees:
        if degree >= 3:
            center_degree = degree
            break

    if center_degree < 3:
        return "No"

    for degree in degrees[1:]:
        if degree == 1:
            center_degree -= 1
            if center_degree < 3:
                return "No"
        elif degree != 2:
            return "No"

    if center_degree == 3 and k == 1:
        return "Yes"
    elif center_degree >= 3 and is_k_multihedgehog(n, k - 1, edges):
        return "Yes"
    else:
        return "No"

# Input parsing
n, k = map(int, input().split())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

print(is_k_multihedgehog(n, k, edges))
```
