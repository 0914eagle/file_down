
def find_smallest_box(n, boxes):
    max_k = max(boxes.keys())
    
    for i in range(max_k, -1, -1):
        if boxes.get(i, 0) > 0:
            for j in range(i-1, -1, -1):
                if boxes.get(j, 0) >= 4**abs(j-i):
                    boxes[j] -= 4**abs(j-i)
            return i

n = int(input())
boxes = {}
for _ in range(n):
    k, a = map(int, input().split())
    boxes[k] = a

print(find_smallest_box(n, boxes))
