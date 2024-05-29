
def find_remaining_number(T, queries):
    results = []
    for query in queries:
        n, x = query
        result = x * 2
        results.append(result)
    return results

T = int(input())
queries = []
for _ in range(T):
    n, x = map(int, input().split())
    queries.append((n, x))

output = find_remaining_number(T, queries)
for res in output:
    print(res)
```
