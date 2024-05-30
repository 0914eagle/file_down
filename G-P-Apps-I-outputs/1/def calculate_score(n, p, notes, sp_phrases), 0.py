
def calculate_score(n, p, notes, sp_phrases):
    score = 0
    sp_meter = 0
    current_note = 0
    
    for i in range(n):
        if current_note < p and notes[i] >= sp_phrases[current_note][0] and notes[i] <= sp_phrases[current_note][1]:
            sp_meter += sp_phrases[current_note][1] - notes[i]
        
        if sp_meter > 0:
            score += 2
        else:
            score += 1
        
        sp_meter = max(0, sp_meter - 1)
        
        if current_note < p and notes[i] == sp_phrases[current_note][1]:
            current_note += 1
    
    return score

# Input parsing
n, p = map(int, input().split())
notes = list(map(int, input().split()))
sp_phrases = [tuple(map(int, input().split())) for _ in range(p)]

# Calculate and print the maximum score
print(calculate_score(n, p, notes, sp_phrases))
```
