
def distinct_characters(s, queries):
    distinct_count = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            distinct_count.append(len(set(s[l-1:r])))
    return distinct_count

# Input processing
s = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    query = list(map(str, input().strip().split()))
    queries.append(list(map(str, query)))

output = distinct_characters(s, queries)
for result in output:
    print(result)
```
