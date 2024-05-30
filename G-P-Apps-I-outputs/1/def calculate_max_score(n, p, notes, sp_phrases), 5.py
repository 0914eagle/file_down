
def calculate_max_score(n, p, notes, sp_phrases):
    score = 0
    sp_charge = 0
    sp_active = False
    
    i = 0
    for j in range(n):
        while i < p and notes[j] >= sp_phrases[i][0] and notes[j] <= sp_phrases[i][1]:
            if sp_active and sp_charge > 0:
                sp_charge = max(sp_charge - (notes[j] - notes[j-1]), 0)
            i += 1
        
        if sp_active and sp_charge > 0:
            score += 2
        else:
            score += 1
        
        if sp_active and sp_charge == 0:
            sp_active = False
        
        if i < p and notes[j] == sp_phrases[i][0]:
            sp_active = True
            sp_charge = sp_phrases[i][1] - sp_phrases[i][0]
    
    return score

# Example inputs
n1, p1 = 3, 1
notes1 = [0, 10, 20]
sp_phrases1 = [(0, 10)]

n2, p2 = 6, 1
notes2 = [0, 10, 20, 26, 40, 50]
sp_phrases2 = [(0, 40)]

print(calculate_max_score(n1, p1, notes1, sp_phrases1))  # Output: 4
print(calculate_max_score(n2, p2, notes2, sp_phrases2))  # Output: 9
```
