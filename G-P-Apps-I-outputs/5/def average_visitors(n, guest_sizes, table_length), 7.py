
import itertools

def average_visitors(n, guest_sizes, table_length):
    total_visitors = 0
    total_orders = 0

    for order in itertools.permutations(guest_sizes):
        curr_sum = 0
        visitors = 0
        for guest_size in order:
            if curr_sum + guest_size <= table_length:
                curr_sum += guest_size
                visitors += 1
            else:
                break
        
        total_visitors += visitors
        total_orders += 1

    return total_visitors / total_orders

# Input reading
n = int(input())
guest_sizes = list(map(int, input().split()))
table_length = int(input())

# Output
result = average_visitors(n, guest_sizes, table_length)
print("{:.10f}".format(result))
```
