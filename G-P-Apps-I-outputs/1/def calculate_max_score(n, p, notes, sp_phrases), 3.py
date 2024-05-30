
def calculate_max_score(n, p, notes, sp_phrases):
    max_score = 0
    sp_active = False
    sp_end_time = 0

    for i in range(n):
        note_time = notes[i]
        if sp_active and note_time > sp_end_time:
            sp_active = False

        if sp_active:
            max_score += 2
        else:
            max_score += 1

        for start, end in sp_phrases:
            if note_time == start:
                sp_active = True
                sp_end_time = end

    return max_score

# Reading input
n, p = map(int, input().split())
notes = list(map(int, input().split()))
sp_phrases = [tuple(map(int, input().split())) for _ in range(p)]

# Calculating and printing the maximum score
print(calculate_max_score(n, p, notes, sp_phrases))
