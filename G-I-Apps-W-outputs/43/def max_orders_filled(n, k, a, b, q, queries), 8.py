
def max_orders_filled(n, k, a, b, q, queries):
    output = []
    current_orders = {day: 0 for day in range(1, n+1)}
    total_filled = 0
    
    for query in queries:
        if query[0] == 1:
            current_orders[query[1]] += query[2]
        elif query[0] == 2:
            total_filled = 0
            for start_day in range(query[1], query[1] + k):
                production = a if start_day >= k else b
                
                orders_to_fill = min(current_orders[start_day], production)
                total_filled += orders_to_fill
                current_orders[start_day] -= orders_to_fill
            
            output.append(total_filled)
    
    return output

# Input parsing
n, k, a, b, q = map(int, input().split())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# Call the function and print the results
output = max_orders_filled(n, k, a, b, q, queries)
for result in output:
    print(result)
```
