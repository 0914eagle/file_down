
def paint_fence(N, offers):
    offers.sort(key=lambda x: (x[1], x[2]))
    
    colors = set()
    accepted_offers = []
    
    for offer in offers:
        color, start, end = offer
        overlap = set()
        
        for accepted_offer in accepted_offers:
            if accepted_offer[2] >= start and accepted_offer[1] <= end:
                overlap.add(accepted_offer[0])
                
        if len(colors.union(overlap)) <= 3:
            colors.add(color)
            accepted_offers.append(offer)
            
    if len(accepted_offers) == 0 or len(colors) > 3:
        return "IMPOSSIBLE"
    else:
        return len(accepted_offers)

# Input parsing
N = int(input())
offers = []
for _ in range(N):
    color, start, end = input().split()
    offers.append((color, int(start), int(end)))

# Call the function and print the result
print(paint_fence(N, offers))
