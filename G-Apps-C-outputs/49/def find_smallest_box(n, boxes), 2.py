
def find_smallest_box(n, boxes):
    max_k = max(boxes, key=lambda x: x[0])[0]
    total_boxes = sum(2 ** k * a for k, a in boxes)
    
    for p in range(max_k + 1):
        if total_boxes <= 2 ** p:
            return p
    
n = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(n)]

print(find_smallest_box(n, boxes))
