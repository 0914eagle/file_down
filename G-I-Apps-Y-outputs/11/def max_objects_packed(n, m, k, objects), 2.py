
def max_objects_packed(n, m, k, objects):
    boxes = [k] * m
    packed_objects = 0
    for obj in objects:
        fit = False
        for i in range(m):
            if boxes[i] >= obj:
                boxes[i] -= obj
                fit = True
                packed_objects += 1
                break
        if not fit:
            break
    return packed_objects

# Reading input
n, m, k = map(int, input().split())
objects = list(map(int, input().split()))

# Call the function and print the output
print(max_objects_packed(n, m, k, objects))
```
