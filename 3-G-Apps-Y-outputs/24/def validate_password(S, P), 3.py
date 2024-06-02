
def validate_password(S, P):
    if S == P:
        return "Yes"
    if len(S) == len(P) + 1 and S[1:] == P:
        return "Yes"
    if len(S) == len(P) + 1 and S[:-1] == P:
        return "Yes"
    if len(S) == len(P) and S.swapcase() == P:
        return "Yes"
    return "No"

# Read input
S = input().strip()
P = input().strip()

# Validate password and print result
print(validate_password(S, P))
