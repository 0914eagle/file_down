
def find_smallest_box(n, boxes):
    max_k = max(boxes.keys())
    total_boxes = sum(boxes.values())

    p = max_k
    while total_boxes > 1:
        p += 1
        total_boxes = (total_boxes + 3) // 4

    return p

# Read input
n = int(input())
boxes = {}
for _ in range(n):
    k, a = map(int, input().split())
    boxes[k] = a

# Find and print the smallest magical box
print(find_smallest_box(n, boxes))
