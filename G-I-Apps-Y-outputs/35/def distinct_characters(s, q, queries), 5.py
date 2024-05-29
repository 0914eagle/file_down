
def distinct_characters(s, q, queries):
    distinct_counts = []
    for i in range(q):
        query_type, *args = queries[i]
        if query_type == 1:
            pos, new_char = args
            s = s[:pos-1] + new_char + s[pos:]
        elif query_type == 2:
            l, r = args
            distinct_chars = set(s[l-1:r])
            distinct_counts.append(len(distinct_chars))
    return distinct_counts

# Reading input
s = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    query = list(map(str, input().strip().split()))
    queries.append(query)

# Performing queries
result = distinct_characters(s, q, queries)

# Output
for res in result:
    print(res)
```
