
def find_smallest_box(n, boxes):
    max_k = max([k for k, _ in boxes])
    total_boxes = sum([2**k * a for k, a in boxes])
    
    smallest_box = 0
    while total_boxes > 0:
        total_boxes >>= 1
        smallest_box += 1

    return max(max_k, smallest_box)

# Input processing
n = int(input())
boxes = []
for _ in range(n):
    k, a = map(int, input().split())
    boxes.append((k, a))

# Call the function and print the result
print(find_smallest_box(n, boxes))
