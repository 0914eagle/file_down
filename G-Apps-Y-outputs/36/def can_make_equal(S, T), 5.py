
def can_make_equal(S, T):
    if len(S) != len(T):
        return "No"
    
    char_map = {}
    
    for char_s, char_t in zip(S, T):
        if char_s not in char_map:
            char_map[char_s] = char_t
        elif char_map[char_s] != char_t:
            return "No"
        
        if char_t not in char_map:
            char_map[char_t] = char_s
        elif char_map[char_t] != char_s:
            return "No"
    
    return "Yes"

S = input().strip()
T = input().strip()
print(can_make_equal(S, T))
