
def max_orders_filled(n, k, a, b, q, queries):
    current_production = b
    max_orders = 0
    order_counts = [0] * (n+1)
    
    for query_type, *args in queries:
        if query_type == 1:
            day, orders = args
            order_counts[day] += orders
        elif query_type == 2:
            day = args[0]
            total_orders = sum(order_counts[day:day+k]) + min(a, current_production) * k
            max_orders = max(max_orders, total_orders)
    
    return max_orders

# Input parsing
n, k, a, b, q = map(int, input().split())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# Calculate and output the maximum orders filled for each query of the second type
for query in queries:
    if query[0] == 2:
        result = max_orders_filled(n, k, a, b, q, queries[:query[0]])
        print(result)
