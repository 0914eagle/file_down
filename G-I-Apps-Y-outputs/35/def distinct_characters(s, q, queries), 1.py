
def distinct_characters(s, q, queries):
    result = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            substring = s[l-1:r]
            unique_chars = len(set(substring))
            result.append(unique_chars)
    return result

# Input parsing
s = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    query = list(map(str, input().strip().split()))
    query = list(map(str, query))
    queries.append(query)

output = distinct_characters(s, q, queries)

for o in output:
    print(o)
```
