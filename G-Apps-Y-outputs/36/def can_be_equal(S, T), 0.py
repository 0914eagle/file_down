
def can_be_equal(S, T):
    if sorted(S) != sorted(T):
        return "No"
    
    char_map = {}
    for s, t in zip(S, T):
        if s in char_map and char_map[s] != t:
            return "No"
        char_map[s] = t
    
    return "Yes"

S = input().strip()
T = input().strip()
print(can_be_equal(S, T))
