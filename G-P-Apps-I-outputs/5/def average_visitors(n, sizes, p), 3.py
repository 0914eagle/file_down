
import itertools

def average_visitors(n, sizes, p):
    total_visitors = 0
    total_orders = 0

    for perm in itertools.permutations(sizes):
        current_size = 0
        visitors = 0
        for size in perm:
            current_size += size
            if current_size <= p:
                visitors += 1
            else:
                break
        total_visitors += visitors
        total_orders += 1

    return total_visitors / total_orders

# Input
n = int(input())
sizes = list(map(int, input().split()))
p = int(input())

# Output
result = average_visitors(n, sizes, p)
print("{:.10f}".format(result))
```
