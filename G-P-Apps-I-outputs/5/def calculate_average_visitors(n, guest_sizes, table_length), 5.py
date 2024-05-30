
def calculate_average_visitors(n, guest_sizes, table_length):
    from itertools import permutations
    
    total_visitors = 0
    total_permutations = 0
    
    for perm in permutations(guest_sizes):
        curr_sum = 0
        visitors = 0
        for guest in perm:
            curr_sum += guest
            if curr_sum <= table_length:
                visitors += 1
            else:
                break
        total_visitors += visitors
        total_permutations += 1

    return total_visitors / total_permutations

# Input
n = 3
guest_sizes = [1, 2, 3]
table_length = 3

result = calculate_average_visitors(n, guest_sizes, table_length)
print(result)
```
