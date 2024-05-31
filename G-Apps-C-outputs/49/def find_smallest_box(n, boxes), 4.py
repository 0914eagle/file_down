
def find_smallest_box(n, boxes):
    max_k = max(boxes, key=lambda x: x[0])[0]
    num_boxes = [0] * (max_k + 1)
    
    for k, a in boxes:
        num_boxes[k] = a
    
    current_boxes = 0
    for i in range(1, max_k + 1):
        current_boxes = (current_boxes + num_boxes[i-1] + 3) // 4
        num_boxes[i] += current_boxes
    
    return max_k

# Input
n = int(input())
boxes = []
for _ in range(n):
    k, a = map(int, input().split())
    boxes.append((k, a))

# Output
print(find_smallest_box(n, boxes))
