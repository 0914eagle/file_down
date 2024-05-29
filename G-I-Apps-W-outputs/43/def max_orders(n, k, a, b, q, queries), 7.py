
def max_orders(n, k, a, b, q, queries):
    orders_per_day = [0] * (n + 1)
    total_orders = 0

    for query in queries:
        if query[0] == 1:
            orders_per_day[query[1]] += query[2]
            total_orders += query[2]
        elif query[0] == 2:
            day_to_start = query[1]
            num_orders = 0

            for i in range(1, n + 1):
                if i >= day_to_start and i <= day_to_start + k - 1:
                    num_orders += min(a, orders_per_day[i])
                else:
                    num_orders += min(b, orders_per_day[i])

            print(num_orders)

n, k, a, b, q = map(int, input().split())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

max_orders(n, k, a, b, q, queries)
```
