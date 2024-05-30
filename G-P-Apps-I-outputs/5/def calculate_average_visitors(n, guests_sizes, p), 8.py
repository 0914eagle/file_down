
import itertools

def calculate_average_visitors(n, guests_sizes, p):
    total_visitors = 0
    possible_orders = list(itertools.permutations(guests_sizes))

    for order in possible_orders:
        sum_sizes = 0
        visitors = 0
        for size in order:
            sum_sizes += size
            if sum_sizes <= p:
                visitors += 1
            else:
                break
        total_visitors += visitors

    return total_visitors / len(possible_orders)

# Input parsing
n = int(input())
guests_sizes = list(map(int, input().split()))
p = int(input())

# Calculate and output the average number of visitors
result = calculate_average_visitors(n, guests_sizes, p)
print("{:.10f}".format(result))
```
