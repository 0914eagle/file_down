
def calculate_max_score(n, p, notes, sp_phrases):
    score = 0
    sp_meter = 0
    sp_active = False

    for i in range(n):
        if sp_active:
            score += 2
        else:
            score += 1

        if i in notes:
            sp_meter += notes[i]

        if sp_active:
            sp_meter -= 1

        if i in sp_phrases:
            sp_active = True

        if sp_meter <= 0:
            sp_active = False
            sp_meter = 0

    return score

# Read input
n, p = map(int, input().split())
notes = {int(x): 0 for x in input().split()}
sp_phrases = {int(input().split()[0]): int(input().split()[1]) for _ in range(p)}

# Calculate and print maximum score
print(calculate_max_score(n, p, notes, sp_phrases))
```
