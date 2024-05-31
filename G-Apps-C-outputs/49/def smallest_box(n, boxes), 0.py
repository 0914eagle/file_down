
def smallest_box(n, boxes):
    max_k = max(boxes, key=lambda x: x[0])[0]
    
    for i in range(max_k, -1, -1):
        total_boxes = sum(a * (2 ** (k - i)) for k, a in boxes if k >= i)
        if total_boxes >= 2 ** i:
            return i
    
    return max_k

n = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(n)]
print(smallest_box(n, boxes))
