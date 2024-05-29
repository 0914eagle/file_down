
def can_create_rectangles(q, queries):
    results = []

    for query in queries:
        n = query[0]
        sticks = query[1]

        sticks.sort()

        area = sticks[0] * sticks[-1]
        valid = True

        for i in range(2*n):
            if sticks[i] * sticks[4*n-1-i] != area or sticks[i] != sticks[i+1]:
                valid = False
                break

        if valid:
            results.append("YES")
        else:
            results.append("NO")

    return results


# Input
q = 5
queries = [
    [1, [1, 1, 10, 10]],
    [2, [10, 5, 2, 10, 1, 1, 2, 5]],
    [2, [10, 5, 1, 10, 5, 1, 1, 1]],
    [2, [1, 1, 1, 1, 1, 1, 1, 1]],
    [1, [10000, 10000, 10000, 10000]]
]

# Output
results = can_create_rectangles(q, queries)
for result in results:
    print(result)
```
