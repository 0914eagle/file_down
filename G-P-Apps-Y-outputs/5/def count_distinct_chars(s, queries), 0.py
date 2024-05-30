
def count_distinct_chars(s, queries):
    distinct_counts = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            distinct_chars = len(set(s[l-1:r]))
            distinct_counts.append(distinct_chars)
    return distinct_counts

# Input processing
s = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    query = list(map(str, input().strip().split()))
    if query[0] == '1':
        queries.append((1, int(query[1]), query[2]))
    elif query[0] == '2':
        queries.append((2, int(query[1]), int(query[2])))

# Solve the problem
result = count_distinct_chars(s, queries)

# Output
for count in result:
    print(count)
```
