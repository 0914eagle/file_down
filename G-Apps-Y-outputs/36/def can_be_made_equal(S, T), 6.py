
def can_be_made_equal(S, T):
    if sorted(S) != sorted(T):
        return "No"

    return "Yes"

S = input().strip()
T = input().strip()

print(can_be_made_equal(S, T))
