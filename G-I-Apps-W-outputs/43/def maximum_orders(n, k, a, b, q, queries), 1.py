
def maximum_orders(n, k, a, b, q, queries):
    orders_filled = [0] * n
    order_updates = {}

    for query in queries:
        if query[0] == 1:
            day, num_orders = query[1], query[2]
            if day in order_updates:
                order_updates[day] += num_orders
            else:
                order_updates[day] = num_orders
        else:
            day_p = query[1]
            for day, orders in order_updates.items():
                if day >= day_p and day <= day_p + k - 1:
                    if a <= b:  # current production rate is enough to fulfill all orders
                        orders_filled[day] += orders
                    else:
                        repairs_left = min(day + k - 1, n - 1) - day + 1  # number of days repairs are left
                        orders_to_fill = min(orders, repairs_left * a)
                        orders_filled[day] += orders_to_fill

    return orders_filled

# Sample input
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

orders_filled = maximum_orders(n, k, a, b, q, queries)
for orders in orders_filled:
    print(orders)
```
