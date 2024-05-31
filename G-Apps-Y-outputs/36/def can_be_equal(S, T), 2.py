
def can_be_equal(S, T):
    if sorted(S) == sorted(T):
        return "Yes"
    return "No"

# Input
S, T = input().split()

# Output
print(can_be_equal(S, T))
