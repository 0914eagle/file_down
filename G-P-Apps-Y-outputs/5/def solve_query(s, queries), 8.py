
def solve_query(s, queries):
    distinct_chars = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        else:
            l, r = query[1], query[2]
            distinct_chars.append(len(set(s[l-1:r])))
    return distinct_chars

# Input parsing
s = input().strip()
q = int(input())
queries = []
for _ in range(q):
    query = list(map(str, input().strip().split()))
    queries.append(list(map(str, query[1:])))

# Solve queries
result = solve_query(s, queries)

# Output the result
for res in result:
    print(res)
```
