
import itertools

def calculate_average_visitors(n, sizes, p):
    total_visitors = 0
    total_orders = 0
    
    for order in itertools.permutations(sizes):
        current_sum = 0
        visitors = 0
        for size in order:
            current_sum += size
            if current_sum <= p:
                visitors += 1
            else:
                break
        total_visitors += visitors
        total_orders += 1
    
    average_visitors = total_visitors / total_orders
    return average_visitors

# Input
n = int(input())
sizes = list(map(int, input().split()))
p = int(input())

# Output
result = calculate_average_visitors(n, sizes, p)
print("{:.10f}".format(result))
```
