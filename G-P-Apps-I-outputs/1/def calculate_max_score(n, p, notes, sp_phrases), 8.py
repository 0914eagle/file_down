
def calculate_max_score(n, p, notes, sp_phrases):
    max_score = 0
    sp_active = False
    sp_remaining_time = 0

    for i in range(n):
        if sp_active:
            max_score += 2
            sp_remaining_time -= notes[i] - notes[i-1]

        if sp_remaining_time <= 0:
            sp_active = False

        if i < p and notes[i] == sp_phrases[i][0]:
            sp_active = True
            sp_remaining_time = sp_phrases[i][1] - sp_phrases[i][0]

    return max_score

# Parse input
n, p = map(int, input().split())
notes = list(map(int, input().split()))
sp_phrases = [tuple(map(int, input().split())) for _ in range(p)]

# Calculate and print the maximum score
print(calculate_max_score(n, p, notes, sp_phrases))
```
