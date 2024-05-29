
def count_distinct_chars(s, queries):
    distinct_counts = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1:]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1:]
            substring = s[l-1:r]
            distinct_counts.append(len(set(substring)))
    return distinct_counts

# Input parsing
s = input().strip()
q = int(input())
queries = []
for _ in range(q):
    query = list(map(str, input().split()))
    if query[0] == '1':
        queries.append((1, int(query[1]), query[2]))
    elif query[0] == '2':
        queries.append((2, int(query[1]), int(query[2])))

# Solve and output
results = count_distinct_chars(s, queries)
for result in results:
    print(result)
```
