
def solve_queries(s, queries):
    distinct_chars = []
    for query in queries:
        if query[0] == 1:  # Replace character at position pos with c
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:  # Calculate number of distinct characters in substring [l:r]
            l, r = query[1], query[2]
            distinct_chars.append(len(set(s[l-1:r])))
    
    return distinct_chars

# Read input
s = input().strip()
q = int(input())
queries = []
for _ in range(q):
    query = list(map(str, input().split()))
    queries.append([int(query[0])] + list(map(int, query[1:])))

# Solve queries
result = solve_queries(s, queries)

# Print output
for ans in result:
    print(ans)
```
