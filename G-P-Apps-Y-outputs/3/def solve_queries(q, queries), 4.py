
def solve_queries(q, queries):
    for query in queries:
        n = query[0]
        p = query[1]

        days_to_return = [0] * n
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                count = 1
                next_idx = p[i] - 1
                while next_idx != i:
                    visited[next_idx] = True
                    count += 1
                    next_idx = p[next_idx] - 1
                days_to_return[i] = count

        print(" ".join(str(x) for x in days_to_return))

# Input processing
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    queries.append((n, p))

solve_queries(q, queries)
```
