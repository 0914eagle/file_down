
def find_smallest_box(n, boxes):
    max_k = max([k for k, _ in boxes])
    total_boxes = sum([a for _, a in boxes])
    smallest_box = 0
    
    while total_boxes > 0:
        if total_boxes % 4 == 0:
            smallest_box = max(smallest_box, max_k)
        else:
            smallest_box = max(smallest_box, max_k + 1)
        
        total_boxes = (total_boxes + 3) // 4
        
        max_k -= 1
    
    return smallest_box

# Input processing
n = int(input())
boxes = []
for _ in range(n):
    k, a = map(int, input().split())
    boxes.append((k, a))

# Find the smallest box
result = find_smallest_box(n, boxes)
print(result)
