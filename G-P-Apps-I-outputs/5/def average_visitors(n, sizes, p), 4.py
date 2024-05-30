
from itertools import permutations

def average_visitors(n, sizes, p):
    total_visitors = 0
    valid_orders = 0
    
    for order in permutations(sizes):
        current_sum = 0
        visitors = 0
        
        for size in order:
            if current_sum + size <= p:
                current_sum += size
                visitors += 1
            else:
                break
        
        total_visitors += visitors
        valid_orders += 1
        
    return total_visitors / valid_orders

# Input
n = int(input())
sizes = list(map(int, input().split()))
p = int(input())

# Output
print("{:.10f}".format(average_visitors(n, sizes, p)))
```
