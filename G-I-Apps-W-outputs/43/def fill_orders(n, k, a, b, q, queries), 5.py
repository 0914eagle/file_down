
def fill_orders(n, k, a, b, q, queries):
    orders = [0] * (n + 1)
    curr_production = b
    filled_orders = 0
    
    for query in queries:
        if query[0] == 1:
            orders[query[1]] += query[2]
        else:
            start_day = query[1]
            for day in range(1, n + 1):
                fillable_orders = min(a, curr_production)
                filled_today = min(orders[day], fillable_orders)
                filled_orders += filled_today
                
                if day >= start_day and day <= start_day + k - 1:
                    curr_production = a
                
                orders[day] -= filled_today
        
            print(filled_orders)
            filled_orders = 0
            curr_production = b
    
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

fill_orders(n, k, a, b, q, queries)
```
