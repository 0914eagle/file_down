
def is_consistent(N, M, matches):
    graph = {}
    for i in range(N):
        graph[i] = set()

    for match in matches:
        k, symbol, l = match
        if symbol == "=":
            if l in graph[k] or k in graph[l]:
                return "inconsistent"
        elif symbol == ">":
            graph[l].add(k)

    return "consistent"

# Reading input
N, M = map(int, input().split())
matches = []
for _ in range(M):
    k, symbol, l = input().split()
    matches.append((int(k), symbol, int(l)))

# Checking consistency
result = is_consistent(N, M, matches)
print(result)
```
