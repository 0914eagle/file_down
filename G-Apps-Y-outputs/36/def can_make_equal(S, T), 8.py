
def can_make_equal(S, T):
    if sorted(S) == sorted(T):
        return "Yes"
    return "No"

# Reading input from Standard Input
S = input()
T = input()

print(can_make_equal(S, T))
