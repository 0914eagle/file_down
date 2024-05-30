
def calculate_max_score(n, p, notes, sp_phrases):
    sp_meters = [0] * (n + 1)
    max_score = 0

    for i in range(1, n + 1):
        sp_meters[i] = sp_meters[i - 1] + 1
        for start, end in sp_phrases:
            if notes[i - 1] >= start and notes[i - 1] <= end:
                sp_meters[i] = max(sp_meters[i], end - notes[i - 1] + sp_meters[next(j for j in range(i - 1, -1, -1) if notes[j] == start)])

        max_score += 2 if sp_meters[i] > 0 else 1

    return max_score

# Reading input
n, p = map(int, input().split())
notes = list(map(int, input().split()))
sp_phrases = [tuple(map(int, input().split())) for _ in range(p)]

# Calculating and printing output
print(calculate_max_score(n, p, notes, sp_phrases))
```
