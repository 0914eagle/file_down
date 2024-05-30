
def calculate_max_score(n, p, notes, sp_phrases):
    score = 0
    sp_meter = 0
    sp_active = False

    for i in range(n):
        if sp_active and sp_meter > 0:
            score += 2
            sp_meter -= notes[i] - notes[i - 1]
        else:
            score += 1
        
        sp_meter = max(sp_meter, 0)

        for start, end in sp_phrases:
            if notes[i] == start:
                sp_active = True
            if notes[i] == end:
                sp_active = False

    return score

# Input parsing
n, p = map(int, input().split())
notes = list(map(int, input().split()))
sp_phrases = [tuple(map(int, input().split())) for _ in range(p)]

# Call the function and print the result
print(calculate_max_score(n, p, notes, sp_phrases))
```
