
def can_be_equal(S, T):
    if sorted(S) != sorted(T):
        return "No"
    
    char_map = {}
    for i in range(len(S)):
        if S[i] in char_map and char_map[S[i]] != T[i]:
            return "No"
        char_map[S[i]] = T[i]
    
    return "Yes"

S, T = input().split()
print(can_be_equal(S, T))
