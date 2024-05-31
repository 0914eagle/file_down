
import math

def smallest_magical_box(n, boxes):
    max_k = max(boxes, key=lambda x: x[0])[0]
    total_boxes = sum([2**k * a for k, a in boxes])
    
    p = math.ceil(math.log2(total_boxes))
    
    return max(max_k, p)

# Read input
n = int(input())
boxes = []
for _ in range(n):
    k, a = map(int, input().split())
    boxes.append((k, a))

# Output result
print(smallest_magical_box(n, boxes))
