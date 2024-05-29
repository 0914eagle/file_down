
def can_create_equal_rectangles(q, queries):
    results = []
    for query in queries:
        n = query[0]
        sticks = sorted(query[1])
        areas = []
        for i in range(2 * n):
            if sticks[i] != sticks[2 * n - i - 1] or sticks[i] * sticks[2 * n - i - 1] != sticks[i + 1] * sticks[2 * n - i - 2]:
                results.append("NO")
                break
            if i % 2 == 1:
                areas.append(sticks[i] * sticks[2 * n - i - 1])
        else:
            if len(set(areas)) == 1:
                results.append("YES")
            else:
                results.append("NO")
    return results

q = 5
queries = [
    (1, [1, 1, 10, 10]),
    (2, [10, 5, 2, 10, 1, 1, 2, 5]),
    (2, [10, 5, 1, 10, 5, 1, 1, 1]),
    (2, [1, 1, 1, 1, 1, 1, 1, 1]),
    (1, [10000, 10000, 10000, 10000])
]

results = can_create_equal_rectangles(q, queries)
for result in results:
    print(result)
```
