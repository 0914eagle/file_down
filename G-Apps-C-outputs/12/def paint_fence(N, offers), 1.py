
def paint_fence(N, offers):
    colors = set()
    sections = set(range(1, 10001))
    
    for color, start, end in offers:
        colors.add(color)
        sections.difference_update(range(start, end + 1))
    
    if len(colors) <= 3 and not sections:
        return len(offers)
    else:
        return "IMPOSSIBLE"

# Reading input
N = int(input())
offers = []
for _ in range(N):
    color, start, end = input().split()
    offers.append((color, int(start), int(end)))

# Calling the function and printing the result
print(paint_fence(N, offers))
