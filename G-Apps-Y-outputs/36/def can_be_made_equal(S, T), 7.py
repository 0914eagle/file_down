
def can_be_made_equal(S, T):
    if sorted(S) == sorted(T):
        return "Yes"
    else:
        return "No"

# Read input
S = input()
T = input()

# Check if S and T can be made equal
result = can_be_made_equal(S, T)
print(result)
