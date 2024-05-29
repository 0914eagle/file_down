
def maximum_orders_filled(n, k, a, b, q, queries):
    production_before = b
    production_after = a
    orders = [0] * n
    filled_orders = [0] * n

    for query in queries:
        if query[0] == 1:
            orders[query[1] - 1] += query[2]
        elif query[0] == 2:
            for i in range(n):
                order_in_hand = min(orders[i], production_before)
                orders[i] -= order_in_hand
                filled_orders[i] += order_in_hand

                if i >= query[1] - 1 and i < query[1] - 1 + k:
                    order_in_hand = min(orders[i], production_after)
                    orders[i] -= order_in_hand
                    filled_orders[i] += order_in_hand

    return max(filled_orders)

# Input parsing
n, k, a, b, q = map(int, input().split())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# Output
for query in queries:
    if query[0] == 2:
        print(maximum_orders_filled(n, k, a, b, q, queries))
