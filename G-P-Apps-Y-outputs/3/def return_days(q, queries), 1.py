
def return_days(q, queries):
    for query in queries:
        n = query[0]
        p = query[1]

        visited = [False] * n
        days = [0] * n

        for i in range(n):
            if not visited[i]:
                curr = i
                day = 1
                while not visited[curr]:
                    visited[curr] = True
                    curr = p[curr] - 1
                    days[curr] = day
                    day += 1

        print(' '.join(map(str, days)))


# Input
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    queries.append((n, p))

# Call the function
return_days(q, queries)
```
