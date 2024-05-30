
from itertools import permutations

def average_visitors(n, sizes, p):
    total_visitors = 0
    total_orders = 0

    for perm in permutations(sizes):
        current_sum = 0
        visitors = 0

        for size in perm:
            current_sum += size
            if current_sum <= p:
                visitors += 1
            else:
                break

        total_visitors += visitors
        total_orders += 1

    return total_visitors / total_orders

# Input parsing
n = int(input())
sizes = list(map(int, input().split()))
p = int(input())

result = average_visitors(n, sizes, p)
print("{:.10f}".format(result))
```
