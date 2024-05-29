
def max_objects_packed(n, m, k, sizes):
    remaining_sizes = [k] * m
    packed_objects = 0

    for size in sizes:
        for i in range(m):
            if size <= remaining_sizes[i]:
                remaining_sizes[i] -= size
                packed_objects += 1
                break
        else:
            continue

    return packed_objects

# Read input
n, m, k = map(int, input().split())
sizes = list(map(int, input().split()))

# Call the function and print the result
print(max_objects_packed(n, m, k, sizes))
```
