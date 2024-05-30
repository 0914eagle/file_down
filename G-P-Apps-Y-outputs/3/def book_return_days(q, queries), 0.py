
def book_return_days(q, queries):
    results = []
    for query in queries:
        n = query[0]
        p = query[1]

        return_days = [0] * n
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue

            cycles = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycles.append(j)
                j = p[j] - 1

            for idx, k in enumerate(cycles):
                return_days[k] = len(cycles)
                if k == cycles[-1]:  # Stop the cycle if we reach the last element of the cycle
                    break

        results.append(return_days)

    return results

# Input
q = 6
queries = [[5, [1, 2, 3, 4, 5]],
           [3, [2, 3, 1]],
           [6, [4, 6, 2, 1, 5, 3]],
           [1, [1]],
           [4, [3, 4, 1, 2]],
           [5, [5, 1, 2, 4, 3]]]

# Output
results = book_return_days(q, queries)
for res in results:
    print(' '.join(map(str, res)))
```
