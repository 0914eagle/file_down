
def build_tree(n, d, k):
    if d >= n:
        return "NO"

    if k < 2:
        return "NO"

    if n == 1:
        return "YES"

    if d == 1:
        if n > 2:
            return "NO"

    if d == 2 and n <= k + 1:
        tree = []
        for i in range(2, n + 1):
            tree.append((1, i))
        return "YES\n" + "\n".join(f"{u} {v}" for u, v in tree)

    if d * k < n:
        return "NO"

    tree = [(i, i + 1) for i in range(1, min(d + 1, n))]
    for v in range(d + 2, n + 1):
        tree.append((v - 1, v))

    return "YES\n" + "\n".join(f"{u} {v}" for u, v in tree)

# Input
n, d, k = map(int, input().split())

# Output
print(build_tree(n, d, k))
```
