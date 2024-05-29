
def check_rectangles(q, queries):
    results = []

    for i in range(q):
        n = queries[i][0]
        sticks = queries[i][1]

        sticks.sort()

        areas = []
        for j in range(2 * n):
            if sticks[j] != sticks[2 * n - 1 - j] or sticks[j * 2] != sticks[j * 2 + 1]:
                results.append("NO")
                break
            area = sticks[j] * sticks[2 * n - 1 - j]
            areas.append(area)

        if len(set(areas)) == 1:
            results.append("YES")
        else:
            results.append("NO")

    return results


# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    sticks = list(map(int, input().split()))
    queries.append((n, sticks))

# Get results
results = check_rectangles(q, queries)

# Output
for result in results:
    print(result)
```
