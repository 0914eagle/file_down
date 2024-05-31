
def can_be_made_equal(S, T):
    if sorted(S) != sorted(T):
        return "No"
    
    s_counter = {}
    t_counter = {}
    for char in S:
        s_counter[char] = s_counter.get(char, 0) + 1
    for char in T:
        t_counter[char] = t_counter.get(char, 0) + 1
    
    if len(s_counter) != len(t_counter):
        return "No"
    
    s_freq = sorted(s_counter.values())
    t_freq = sorted(t_counter.values())
    
    if s_freq != t_freq:
        return "No"
    
    return "Yes"

# Input
S, T = input().split()

# Output
print(can_be_made_equal(S, T))
