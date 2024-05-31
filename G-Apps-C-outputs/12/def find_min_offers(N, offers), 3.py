
def find_min_offers(N, offers):
    offers.sort(key=lambda x: x[1])
    
    colors_set = set()
    accepted_offers = []
    
    for offer in offers:
        color, start, end = offer
        temp_set = colors_set.copy()
        
        for c in temp_set:
            if (start <= c[0] <= end) or (start <= c[1] <= end) or (c[0] <= start <= c[1]) or (c[0] <= end <= c[1]):
                colors_set.remove(c)
        
        colors_set.add((start, end))
        accepted_offers.append(offer)
        
        if len(colors_set) > 3:
            return "IMPOSSIBLE"
    
    return len(accepted_offers)

# Input processing
N = int(input())
offers = []
for _ in range(N):
    C, A, B = input().split()
    A, B = int(A), int(B)
    offers.append((C, A, B))

# Call the function and print the output
result = find_min_offers(N, offers)
print(result)
