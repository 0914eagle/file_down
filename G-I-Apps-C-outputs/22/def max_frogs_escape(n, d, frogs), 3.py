
def max_frogs_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)
    res = 0
    piles = []
    
    for i in range(n):
        frog = frogs[i]
        placed = False
        
        for pile in piles:
            if sum(p[1] for p in pile) >= frog[1]:
                continue
            else:
                placed = True
                pile.append(frog)
                break
                
        if not placed:
            piles.append([frog])
            
    for pile in piles:
        stack_height = sum(p[2] for p in pile) + sum(p[1] for p in pile)
        if stack_height >= d:
            res += len(pile)
    
    return res

# Input parsing
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_frogs_escape(n, d, frogs))
```
