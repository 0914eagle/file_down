
def min_offers_to_accept(N, offers):
    def dfs(start, colors_used, offers_accepted):
        if start == 10001:
            return offers_accepted if len(colors_used) <= 3 else float('inf')
        
        skip = dfs(start + 1, colors_used, offers_accepted)
        
        for offer in offers:
            color, a, b = offer
            if a <= start <= b:
                new_colors_used = colors_used | {color}
                new_offers_accepted = offers_accepted + 1
                skip = min(skip, dfs(b + 1, new_colors_used, new_offers_accepted))
        
        return skip
    
    offers.sort(key=lambda x: x[1])
    result = dfs(1, set(), 0)
    
    return result if result != float('inf') else "IMPOSSIBLE"

# Input reading
N = int(input())
offers = []
for _ in range(N):
    color, a, b = input().split()
    offers.append((color, int(a), int(b)))

# Call the function and print the result
print(min_offers_to_accept(N, offers))
