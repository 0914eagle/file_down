
import itertools

def calculate_average_visitors(n, guests, p):
    total_visitors = 0
    total_orders = 0
    
    for order in itertools.permutations(guests):
        table_space = p
        visitors = 0
        for guest in order:
            if guest <= table_space:
                table_space -= guest
                visitors += 1
            else:
                break
        total_visitors += visitors
        total_orders += 1
    
    return total_visitors / total_orders

# Input
n = int(input())
guests = list(map(int, input().split()))
p = int(input())

# Output
result = calculate_average_visitors(n, guests, p)
print('{:.10f}'.format(result))
```
