
def solve_thimbles_problem(n, k, a, b, q, queries):
    production = [a] * n
    for query in queries:
        if query[0] == 1:
            day, orders = query[1], query[2]
            production[day - 1] = min(production[day - 1], b)
        elif query[0] == 2:
            start_day = query[1]
            max_orders = 0
            for i in range(start_day - 1, start_day + k - 1):
                max_orders += min(production[i], b)
            print(max_orders)

# Example input
n, k, a, b, q = 5, 2, 2, 1, 8
queries = [
    [1, 1, 2],
    [1, 5, 3],
    [1, 2, 1],
    [2, 2],
    [1, 4, 2],
    [1, 3, 2],
    [2, 1],
    [2, 3]
]

solve_thimbles_problem(n, k, a, b, q, queries)
```
