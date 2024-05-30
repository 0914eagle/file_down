
def count_transformations(n, q, operations):
    def dfs(s, idx):
        if idx == n-1:
            return 1 if s == 'a' else 0
        count = 0
        for a, b in operations:
            if s.startswith(a):
                count += dfs(b + s[2:], idx + 1)
        return count

    initial_strings = [''.join(c) for c in itertools.product('abcdef', repeat=n)]
    total_count = 0
    for s in initial_strings:
        total_count += dfs(s, 0)

    return total_count

# Input parsing
n, q = map(int, input().split())
operations = []
for _ in range(q):
    a, b = input().split()
    operations.append((a, b))

result = count_transformations(n, q, operations)
print(result)
```
