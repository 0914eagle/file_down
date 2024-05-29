
def max_orders_filled(n, k, a, b, q, queries):
    orders = [0] * n
    for query in queries:
        if query[0] == 1:
            orders[query[1] - 1] += query[2]
    
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + min(a, orders[i - 1])
    
    max_orders = prefix_sum[k]
    for i in range(1, n - k + 1):
        window_orders = prefix_sum[i + k] - prefix_sum[i]
        max_orders = max(max_orders, window_orders)
    
    return max_orders

# Input parsing
n, k, a, b, q = map(int, input().split())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# Process queries of type 2 and output the result
for query in queries:
    if query[0] == 2:
        result = max_orders_filled(n, k, a, b, q, queries)
        print(result)
```
