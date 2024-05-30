
def return_days(q, queries):
    res = []
    for query in queries:
        n = query[0]
        p = query[1]

        days_to_return = [0] * n
        for i in range(n):
            visited = set()
            curr = i
            day = 1
            while curr not in visited:
                visited.add(curr)
                curr = p[curr] - 1
                day += 1
            days_to_return[i] = day - 1

        res.append(days_to_return)

    return res

# Input
q = 6
queries = [
    [5, [1, 2, 3, 4, 5]],
    [3, [2, 3, 1]],
    [6, [4, 6, 2, 1, 5, 3]],
    [1, [1]],
    [4, [3, 4, 1, 2]],
    [5, [5, 1, 2, 4, 3]]
]

# Output
output = return_days(q, queries)
for res in output:
    print(' '.join(map(str, res)))
```
