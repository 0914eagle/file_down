
def max_packed_objects(n, m, k, objects):
    boxes = [k] * m
    packed = 0
    i = 0

    while i < n:
        for j in range(m):
            if objects[i] <= boxes[j]:
                boxes[j] -= objects[i]
                packed += 1
                i += 1
                if i == n:
                    break

    return packed

# Read input
n, m, k = map(int, input().split())
objects = list(map(int, input().split()))

# Find and print the maximum number of objects Maksim can pack
print(max_packed_objects(n, m, k, objects))
```
