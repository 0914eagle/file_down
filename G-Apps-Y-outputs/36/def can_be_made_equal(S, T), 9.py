
def can_be_made_equal(S, T):
    if sorted(S) != sorted(T):
        return "No"

    letter_map = {}
    for s, t in zip(S, T):
        if s in letter_map and letter_map[s] != t:
            return "No"
        letter_map[s] = t

    return "Yes"

# Input
S = input().strip()
T = input().strip()

# Output
print(can_be_made_equal(S, T))
