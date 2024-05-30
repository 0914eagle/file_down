
def calculate_max_score(n, p, notes, sp_phrases):
    score = 0
    sp_active = False
    sp_time = 0

    for i in range(n):
        if sp_active:
            score += 2
            sp_time -= 1
            if sp_time == 0:
                sp_active = False

        if i in notes:
            score += 1

        for sp in sp_phrases:
            if sp[0] <= i <= sp[1]:
                sp_active = True
                sp_time = sp[1] - i

    return score

# Input parsing
n, p = map(int, input().split())
notes = list(map(int, input().split()))
sp_phrases = [list(map(int, input().split())) for _ in range(p)]

# Calculate and print the maximum score
print(calculate_max_score(n, p, notes, sp_phrases))
```
