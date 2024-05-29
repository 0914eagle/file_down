
def distinct_characters(s, q, queries):
    unique_chars_count = []
    
    for query in queries:
        if query[0] == 2:
            l, r = query[1], query[2]
            substr = s[l-1:r]
            unique_chars = len(set(substr))
            unique_chars_count.append(unique_chars)
        elif query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
    
    return unique_chars_count

# Input parsing
s = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    query = input().strip().split()
    query_type = int(query[0])
    if query_type == 1:
        queries.append((1, int(query[1]), query[2]))
    elif query_type == 2:
        queries.append((2, int(query[1]), int(query[2])))

# Call the function
result = distinct_characters(s, q, queries)

# Output
for res in result:
    print(res)
```
