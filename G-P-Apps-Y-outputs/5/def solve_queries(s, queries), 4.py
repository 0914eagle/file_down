
def solve_queries(s, queries):
    distinct_chars = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            distinct_chars.append(len(set(s[l-1:r])))
    return distinct_chars

# Input parsing
s = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    query = list(map(str, input().strip().split()))
    if query[0] == '1':
        queries.append((1, int(query[1]), query[2]))
    else:
        queries.append((2, int(query[1]), int(query[2])))

# Solve queries
results = solve_queries(s, queries)

# Output results
for result in results:
    print(result)
```
