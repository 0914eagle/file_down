
def max_frogs_to_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)
    escaped_frogs = 0
    piles = []
    
    for frog in frogs:
        pile_index = -1
        for i, pile in enumerate(piles):
            if sum(p[1] for p in pile) >= frog[1]:
                continue
            if pile_index == -1 or pile[-1][2] < pile[pile_index][-1][2]:
                pile_index = i
        
        if pile_index != -1:
            piles[pile_index].append(frog)
        elif frog[0] >= d:
            escaped_frogs += 1
        else:
            piles.append([frog])
    
    total_frogs = sum(len(pile) for pile in piles)
    
    return escaped_frogs + min(total_frogs, n - escaped_frogs)

# Read input
n, d = map(int, input().split())
frogs = []
for _ in range(n):
    l, w, h = map(int, input().split())
    frogs.append((l, w, h))

# Call the function
result = max_frogs_to_escape(n, d, frogs)
print(result)
```
