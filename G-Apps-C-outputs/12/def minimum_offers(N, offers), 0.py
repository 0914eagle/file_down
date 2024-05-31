
def minimum_offers(N, offers):
    offers.sort(key=lambda x: (x[1], x[2]))  # Sort offers by starting section
    
    # Initialize variables
    colors_used = set()
    accepted_offers = []
    
    # Iterate through offers
    for color, start, end in offers:
        if len(colors_used) == 3:  # Already using 3 colors
            return "IMPOSSIBLE"
        
        if color in colors_used:  # Color already used
            continue
        
        accepted_offers.append((color, start, end))
        colors_used.add(color)
    
    return len(accepted_offers)

# Read input
N = int(input())
offers = []
for _ in range(N):
    color, start, end = input().split()
    offers.append((color, int(start), int(end)))

# Call the function and print the result
result = minimum_offers(N, offers)
print(result)
