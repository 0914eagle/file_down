
def solve_queries(s, q, queries):
    distinct_chars = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            distinct_chars.append(len(set(s[l-1:r])))
    return distinct_chars

# Input
s = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    query = list(map(str, input().strip().split()))
    queries.append(list(map(int, query[1:])) if query[0] == '2' else list(map(str, query[1:])))

# Solve queries and output results
output = solve_queries(s, q, queries)
for result in output:
    print(result)
```
