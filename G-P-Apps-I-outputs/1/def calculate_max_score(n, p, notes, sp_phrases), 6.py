
def calculate_max_score(n, p, notes, sp_phrases):
    score = 0
    sp_charge = 0
    sp_active = False
    sp_end = 0
    
    for i in range(n):
        if sp_active and sp_charge > 0:
            score += 2
            sp_charge -= 1
        else:
            score += 1
        
        if notes[i] == sp_end:
            sp_active = False
            sp_charge = 0
        
        for start, end in sp_phrases:
            if notes[i] == start:
                sp_active = True
                sp_charge += end - start
                sp_end = end
    
    return score

# Input processing
n, p = map(int, input().split())
notes = list(map(int, input().split()))
sp_phrases = [tuple(map(int, input().split())) for _ in range(p)]

# Output the result
print(calculate_max_score(n, p, notes, sp_phrases))
```
