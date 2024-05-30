
def solve_queries(q, queries):
    for query in queries:
        n = query[0]
        p = query[1]

        visited = [False] * n
        days = [0] * n

        for i in range(n):
            if not visited[i]:
                visited_set = set()
                j = i
                while not visited[j]:
                    visited_set.add(j)
                    visited[j] = True
                    j = p[j] - 1

                for k in visited_set:
                    days[k] = len(visited_set)

        print(*days)

# Example usage
test_input = [
    (5, [1, 2, 3, 4, 5]),
    (3, [2, 3, 1]),
    (6, [4, 6, 2, 1, 5, 3]),
    (1, [1]),
    (4, [3, 4, 1, 2]),
    (5, [5, 1, 2, 4, 3])
]

solve_queries(len(test_input), test_input)
```
