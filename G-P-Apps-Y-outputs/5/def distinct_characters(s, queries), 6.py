
def distinct_characters(s, queries):
    distinct_chars = []
    for query in queries:
        if query[0] == 1:
            pos, char = query[1], query[2]
            s = s[:pos-1] + char + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            distinct_chars.append(len(set(s[l-1:r])))
    return distinct_chars

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

# Call the function with input
output = distinct_characters(s, queries)

# Output
for result in output:
    print(result)
```
