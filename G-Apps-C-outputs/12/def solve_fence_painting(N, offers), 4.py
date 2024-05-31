
def solve_fence_painting(N, offers):
    offers.sort(key=lambda x: (x[1], x[2]))
    
    color_count = {}
    sections_covered = set()
    accepted_offers = []
    
    for offer in offers:
        color, start, end = offer
        if all(k in color_count for k in color_count) and len(color_count) == 3:
            break
        
        sections = set(range(start, end + 1))
        if sections.intersection(sections_covered):
            continue
        
        accepted_offers.append(offer)
        sections_covered.update(sections)
        color_count[color] = color_count.get(color, 0) + 1
    
    if len(sections_covered) == 10000 and len(color_count) <= 3:
        return len(accepted_offers)
    else:
        return "IMPOSSIBLE"

# Input parsing
N = int(input())
offers = []
for _ in range(N):
    color, start, end = input().split()
    start, end = int(start), int(end)
    offers.append((color, start, end))

# Call the function and print the result
result = solve_fence_painting(N, offers)
print(result)
