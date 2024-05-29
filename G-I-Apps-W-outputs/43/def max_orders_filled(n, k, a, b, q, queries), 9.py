
def max_orders_filled(n, k, a, b, q, queries):
    orders = [0] * (n + 1)
    for query in queries:
        if query[0] == 1:
            orders[query[1]] += query[2]

    prefix_sum = [0] * (n + k + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + orders[i]
    
    for i in range(n + 1, n + k + 1):
        prefix_sum[i] = prefix_sum[i - 1]
    
    max_orders = max(prefix_sum[k:])
    
    for query in queries:
        if query[0] == 2:
            p = query[1]
            max_filled = min((p - 1) * a + prefix_sum[p - 1], max_orders, p * b + prefix_sum[p + k - 1])
            print(max_filled)

# Example input
n, k, a, b, q = 5, 2, 2, 1, 8
queries = [
    (1, 1, 2),
    (1, 5, 3),
    (1, 2, 1),
    (2, 2),
    (1, 4, 2),
    (1, 3, 2),
    (2, 1),
    (2, 3)
]

max_orders_filled(n, k, a, b, q, queries)
```
