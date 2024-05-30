
def max_prettiness_contest(q, queries):
    results = []
    for query in queries:
        n = query[0]
        a = query[1]

        a.sort(reverse=True)
        ans = 0

        for i in range(min(3, n)):
            for j in range(i+1, min(3, n)):
                for k in range(j+1, min(3, n)):
                    if a[i] % a[j] != 0 and a[j] % a[k] != 0 and a[i] % a[k] != 0:
                        ans = max(ans, a[i] + a[j] + a[k])

        results.append(ans)

    return results

# Input
q = 3
queries = [(4, [5, 6, 15, 30]), (4, [10, 6, 30, 15]), (3, [3, 4, 6])]

# Output
output = max_prettiness_contest(q, queries)
for res in output:
    print(res)
```
