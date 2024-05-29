
def max_objects_packed(n, m, k, a):
    total_objects = 0
    boxes_remaining_space = [k] * m
    current_box_index = 0

    for i in range(n):
        if a[i] <= boxes_remaining_space[current_box_index]:
            boxes_remaining_space[current_box_index] -= a[i]
            total_objects += 1
        else:
            current_box_index += 1
            if current_box_index == m:
                break
            current_box_index %= m
            boxes_remaining_space[current_box_index] = k - a[i]
            total_objects += 1

    return total_objects

# Input parsing
n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the result
print(max_objects_packed(n, m, k, a))
```
