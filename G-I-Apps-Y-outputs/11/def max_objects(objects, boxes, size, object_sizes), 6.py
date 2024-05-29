
def max_objects(objects, boxes, size, object_sizes):
    objects_packed = 0
    objects_to_pack = object_sizes
    remaining_boxes = boxes
    
    while objects_to_pack:
        if objects_to_pack[0] <= size:
            objects_packed += 1
            remaining_boxes -= 1
            objects_to_pack.pop(0)
        elif remaining_boxes > 0:
            remaining_boxes = boxes
        else:
            break
            
    return objects_packed

# Input
n, m, k = map(int, input().split())
object_sizes = list(map(int, input().split()))

# Output
print(max_objects(n, m, k, object_sizes))
```
