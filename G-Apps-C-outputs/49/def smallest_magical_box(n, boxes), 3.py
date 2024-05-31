
def smallest_magical_box(n, boxes):
    max_k = max([k for k, _ in boxes])
    
    total_boxes = 0
    for k, a in boxes:
        total_boxes += a * (2 ** (max_k - k))
    
    p = 0
    while total_boxes > 0:
        total_boxes //= 4
        p += 1
    
    return max_k + p

# Reading input
n = int(input())
boxes = []
for _ in range(n):
    k, a = map(int, input().split())
    boxes.append((k, a))

# Calling the function and printing the result
print(smallest_magical_box(n, boxes))
