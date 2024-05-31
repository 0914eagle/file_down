
def minimum_offers(N, offers):
    offers.sort(key=lambda x: x[1])
    
    colors = set()
    sections = set(range(1, 10001))
    accepted_offers = []
    
    for offer in offers:
        color, start, end = offer
        
        if len(colors) == 3:
            return "IMPOSSIBLE"
        
        if any(x in sections for x in range(start, end+1)):
            colors.add(color)
            accepted_offers.append(offer)
            sections.difference_update(range(start, end+1))
    
    return len(accepted_offers)

# Input parsing
N = int(input())
offers = []
for _ in range(N):
    color, start, end = input().split()
    offers.append((color, int(start), int(end)))

# Call the function and print the result
result = minimum_offers(N, offers)
print(result)
