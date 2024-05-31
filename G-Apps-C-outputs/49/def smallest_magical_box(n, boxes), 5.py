
def smallest_magical_box(n, boxes):
    max_k = max(boxes, key=lambda x: x[0])[0]
    total_boxes = sum(2 ** k * a for k, a in boxes)
    
    p = 0
    while (1 << p) < total_boxes:
        p += 1
    
    return max(p, max_k)

# Input
n = int(input())
boxes = []
for _ in range(n):
    k, a = map(int, input().split())
    boxes.append((k, a))

# Output
print(smallest_magical_box(n, boxes))
