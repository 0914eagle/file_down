
def max_orders_filled(n, k, a, b, q, queries):
    thimbles_per_day = [a] * n
    for query in queries:
        if query[0] == 1:
            thimbles_per_day[query[1] - 1] = min(a, thimbles_per_day[query[1] - 1] + query[2])
    
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + min(thimbles_per_day[i - 1], b)
    
    max_orders = 0
    for query in queries:
        if query[0] == 2:
            max_orders = max(max_orders, prefix_sum[query[1] + k - 1] - prefix_sum[query[1] - 1])
    return max_orders

# Input processing
n, k, a, b, q = map(int, input().split())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

result = max_orders_filled(n, k, a, b, q, queries)
print(result)
