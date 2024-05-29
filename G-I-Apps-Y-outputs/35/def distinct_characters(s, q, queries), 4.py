
def distinct_characters(s, q, queries):
    res = []
    substr = set(s)
    
    for query in queries:
        if query[0] == 1:
            s = s[:query[1]-1] + query[2] + s[query[1]:]
        elif query[0] == 2:
            res.append(len(set(s[query[1]-1:query[2]])))
    
    return res

# Read input
s = input()
q = int(input())
queries = []
for _ in range(q):
    query = input().split()
    query = list(map(lambda x: int(x) if x.isdigit() else x, query))
    queries.append(query)

# Solve
results = distinct_characters(s, q, queries)

# Output results
for result in results:
    print(result)
``` 
