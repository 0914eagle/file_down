
def max_objects_packed(n, m, k, objects):
    filled_boxes = 0
    total_objects_packed = 0
    remaining_object_sizes = objects[:]
    
    for obj_size in objects:
        if obj_size > k:
            break
        
        if filled_boxes == m:
            break
        
        if obj_size <= k:
            filled_boxes += 1
            remaining_object_sizes.pop(0)
        else:
            break
            
    total_objects_packed = len(objects) - len(remaining_object_sizes)
    
    return total_objects_packed

# Input parsing
n, m, k = map(int, input().split())
objects = list(map(int, input().split()))

# Call the function and print the result
print(max_objects_packed(n, m, k, objects))
```
