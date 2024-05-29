
def construct_tree(n, d, k):
    if d >= n:
        return "NO"

    if k < 2:
        return "NO"

    tree = []
    curr_vertex = 1

    for i in range(2, min(n, d + 2)):
        tree.append((curr_vertex, i))
        curr_vertex = i

    if d + 1 < n:
        for i in range(d + 2, n + 1):
            tree.append((2, i))

    return "YES\n" + "\n".join([f"{x} {y}" for x, y in tree])

n, d, k = map(int, input().split())
print(construct_tree(n, d, k))
```
