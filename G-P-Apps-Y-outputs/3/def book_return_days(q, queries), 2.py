
def book_return_days(q, queries):
    res = []
    for query in queries:
        n = query[0]
        p = query[1]
        days = [0] * n
        for i in range(n):
            visited = set()
            curr = i
            day = 1
            while curr not in visited:
                visited.add(curr)
                curr = p[curr] - 1
                day += 1
            days[i] = day - 1
        res.append(days)
    return res

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    queries.append((n, p))

# Call the function with the input
output = book_return_days(q, queries)

# Output the result
for query_output in output:
    print(*query_output)
```
