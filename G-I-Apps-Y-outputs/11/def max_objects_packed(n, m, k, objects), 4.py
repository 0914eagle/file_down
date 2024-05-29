
def max_objects_packed(n, m, k, objects):
    total_objects = 0
    remaining_capacity = [k] * m
    for obj_size in objects:
        if obj_size <= min(remaining_capacity):
            idx = remaining_capacity.index(min(remaining_capacity))
            remaining_capacity[idx] -= obj_size
            total_objects += 1
        else:
            break
    return total_objects

# Read input
n, m, k = map(int, input().split())
objects = list(map(int, input().split()))

# Calculate and print the maximum number of objects that Maksim can pack
print(max_objects_packed(n, m, k, objects))
```
