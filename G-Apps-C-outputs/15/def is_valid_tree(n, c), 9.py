
def is_valid_tree(n, c):
    total_nodes = sum(c)
    if total_nodes != n:
        return "NO"

    for i in range(n):
        if c[i] > i:
            return "NO"

    return "YES"

n = int(input())
c = list(map(int, input().split()))

result = is_valid_tree(n, c)
print(result)
