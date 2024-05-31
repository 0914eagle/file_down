
def paint_fence(N, offers):
    offers.sort(key=lambda x: (x[1], x[2]))
    
    color_count = {}
    for color, start, end in offers:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += end - start + 1
    
    colors = sorted(color_count.keys(), key=lambda x: color_count[x], reverse=True)
    
    if len(colors) > 3:
        return "IMPOSSIBLE"
    
    accepted_offers = []
    total_sections = 0
    for color in colors:
        total_sections += color_count[color]
        accepted_offers.append(color)
        if total_sections >= 10000:
            return len(accepted_offers)
    
    return "IMPOSSIBLE"


# Input parsing
N = int(input())
offers = []
for _ in range(N):
    color, start, end = input().split()
    offers.append((color, int(start), int(end)))

result = paint_fence(N, offers)
print(result)
