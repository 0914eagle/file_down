
def max_objects_packed(n, m, k, object_sizes):
    objects_packed = 0
    boxes = [k] * m
    i = 0

    while i < n:
        if object_sizes[i] <= boxes[0]:
            boxes[0] -= object_sizes[i]
            objects_packed += 1
        else:
            if m > 1:
                m -= 1
                boxes = [k] * m
                boxes[0] -= object_sizes[i]
                objects_packed = 1
            else:
                break
        i += 1

    return objects_packed

# Input
n, m, k = map(int, input().split())
object_sizes = list(map(int, input().split()))

# Output
print(max_objects_packed(n, m, k, object_sizes))
```
