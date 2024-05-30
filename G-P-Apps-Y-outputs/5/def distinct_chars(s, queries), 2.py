
def distinct_chars(s, queries):
    ans = []
    for query in queries:
        if query[0] == 2:
            l, r = query[1], query[2]
            ans.append(len(set(s[l-1:r])))
        else:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
    return ans

# Input parsing
s = input().strip()
q = int(input())
queries = []
for _ in range(q):
    query = list(map(str, input().split()))
    queries.append(list(map(int, query)))

# Solve the problem
output = distinct_chars(s, queries)

# Output the result
for value in output:
    print(value)
```
