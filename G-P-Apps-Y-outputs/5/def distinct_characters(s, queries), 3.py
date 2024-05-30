
def distinct_characters(s, queries):
    distinct_chars = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            distinct_chars.append(len(set(s[l-1:r])))
    return distinct_chars

# Input processing
s = input().strip()
q = int(input())
queries = []
for _ in range(q):
    query = list(map(str, input().split()))
    query[1] = int(query[1])
    if len(query) == 3:
        query[2] = query[2]
    queries.append(query)

result = distinct_characters(s, queries)
for res in result:
    print(res)
``` 
