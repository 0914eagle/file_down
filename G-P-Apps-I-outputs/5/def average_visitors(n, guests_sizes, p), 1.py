
from itertools import permutations

def average_visitors(n, guests_sizes, p):
    total_visitors = 0
    total_permutations = 0
    
    for perm in permutations(guests_sizes):
        current_sum = 0
        visitors = 0
        for guest_size in perm:
            if current_sum + guest_size <= p:
                current_sum += guest_size
                visitors += 1
            else:
                break
        total_visitors += visitors
        total_permutations += 1
    
    return total_visitors / total_permutations

# Input processing
n = int(input())
guests_sizes = list(map(int, input().split()))
p = int(input())

result = average_visitors(n, guests_sizes, p)
print("{:.10f}".format(result))
```
