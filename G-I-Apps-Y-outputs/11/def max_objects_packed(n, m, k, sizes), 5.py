
def max_objects_packed(n, m, k, sizes):
    total_objects = 0
    boxes = [k] * m
    used_boxes = 0
    i = 0
    
    while i < n:
        if used_boxes == m:
            break
        
        if sizes[i] <= boxes[used_boxes]:
            boxes[used_boxes] -= sizes[i]
            total_objects += 1
            i += 1
        else:
            used_boxes += 1
    
    return total_objects

# Reading input
n, m, k = map(int, input().split())
sizes = list(map(int, input().split()))

# Calling the function and printing the result
result = max_objects_packed(n, m, k, sizes)
print(result)
```
