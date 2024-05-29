
def distinct_characters(s, queries):
    distinct_counts = []
    for query in queries:
        if query[0] == 1:
            pos = query[1]
            new_char = query[2]
            s = s[:pos-1] + new_char + s[pos:]
        elif query[0] == 2:
            l = query[1]
            r = query[2]
            substring = s[l-1:r]
            distinct_chars = set(substring)
            distinct_counts.append(len(distinct_chars))
    return distinct_counts

# Read input
s = input().strip()
q = int(input())

queries = []
for _ in range(q):
    query = list(map(str, input().split()))
    if query[0] == '1':
        queries.append((1, int(query[1]), query[2]))
    elif query[0] == '2':
        queries.append((2, int(query[1]), int(query[2])))

result = distinct_characters(s, queries)

for count in result:
    print(count)
```
