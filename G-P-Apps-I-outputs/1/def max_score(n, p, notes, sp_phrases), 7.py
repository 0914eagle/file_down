
def max_score(n, p, notes, sp_phrases):
    sp_charging = 0
    score = 0
    for i in range(n-1):
        time_diff = notes[i+1] - notes[i]
        score += time_diff // 10
        
        for start, end in sp_phrases:
            if notes[i] >= start and notes[i] < end:
                sp_charging += time_diff
        
        if sp_charging > 0:
            score += time_diff // 5
            sp_charging -= time_diff
    
    return score

# Reading input
n, p = map(int, input().split())
notes = list(map(int, input().split()))
sp_phrases = [tuple(map(int, input().split())) for _ in range(p)]

# Calculating and printing the maximum score
print(max_score(n, p, notes, sp_phrases))
```
