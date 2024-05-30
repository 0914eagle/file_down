
def max_prettiness_contest(q, queries):
    results = []
    for query in queries:
        n = query[0]
        a = query[1]
        a.sort(reverse=True)

        max_prettiness = 0

        # Case 1: Choosing one problem
        max_prettiness = max(max_prettiness, a[0])

        # Case 2: Choosing two problems
        for i in range(n - 1):
            for j in range(i + 1, n):
                if a[i] % a[j] != 0 and a[j] % a[i] != 0:
                    max_prettiness = max(max_prettiness, a[i] + a[j])

        # Case 3: Choosing three problems
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if a[i] % a[j] != 0 and a[j] % a[i] != 0 and a[i] % a[k] != 0 and a[k] % a[i] != 0 and a[j] % a[k] != 0 and a[k] % a[j] != 0:
                        max_prettiness = max(max_prettiness, a[i] + a[j] + a[k])

        results.append(max_prettiness)

    return results

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    queries.append((n, a))

# Calculate and output results
results = max_prettiness_contest(q, queries)
for result in results:
    print(result)
```
