
def book_return_days(q, queries):
    res = []
    for i in range(q):
        n = queries[i][0]
        p = queries[i][1]
        a = [0] * n
        for j in range(n):
            visited = set()
            day = 1
            curr = j
            while p[curr] not in visited:
                visited.add(curr)
                curr = p[curr] - 1
                day += 1
            a[j] = day
        res.append(a)
    return res

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    queries.append((n, p))

# Call the function and print the output
output = book_return_days(q, queries)
for ans in output:
    print(' '.join(map(str, ans)))
```
