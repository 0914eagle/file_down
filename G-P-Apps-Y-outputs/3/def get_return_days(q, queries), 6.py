
def get_return_days(q, queries):
    res = []
    for query in queries:
        n = query[0]
        p = query[1]

        touched = [False] * n
        days = [0] * n

        for i in range(n):
            if not touched[i]:
                cur = i
                day = 1
                while not touched[cur]:
                    touched[cur] = True
                    cur = p[cur] - 1
                    days[cur] = day
                    day += 1

        res.append(days)

    return res


# Input
queries = [
    (5, [1, 2, 3, 4, 5]),
    (3, [2, 3, 1]),
    (6, [4, 6, 2, 1, 5, 3]),
    (1, [1]),
    (4, [3, 4, 1, 2]),
    (5, [5, 1, 2, 4, 3])
]

q = 6

# Output
output = get_return_days(q, queries)

for line in output:
    print(" ".join(map(str, line)))
```
