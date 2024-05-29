
def construct_tree(n, d, k):
    if d >= n:
        return "NO"

    if n == 1:
        return "YES\n1"

    if k == 1:
        return "NO"

    if d == 1:
        if n == 2:
            return "YES\n1 2"
        else:
            return "NO"

    if d > 2 * k:
        return "NO"

    tree = []
    start = 2
    for i in range(2, min(d + 1, n - k + 1)):
        tree.append((1, i))
        start = i + 1

    for i in range(start, n + 1):
        tree.append((i, (i - 1) % k + 2))

    if len(tree) >= n:
        return "NO"
    while len(tree) < n - 1:
        tree.append((2, start))
        start += 1

    result = "YES\n" + "\n".join(f"{u} {v}" for u, v in tree)
    return result

# Input example: 6 3 3
n, d, k = map(int, input().split())
print(construct_tree(n, d, k))
