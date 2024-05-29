
def count_distinct_chars(s, queries):
    distinct_counts = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            distinct_chars = set(s[l-1:r])
            distinct_counts.append(len(distinct_chars))
    return distinct_counts

# Input parsing
s = input().strip()
q = int(input())
queries = []
for _ in range(q):
    query = list(map(str, input().split()))
    query = list(map(lambda x: int(x) if x.isdigit() else x, query))
    queries.append(query)

# Execute queries and print the output
result = count_distinct_chars(s, queries)
for res in result:
    print(res)
``` 
