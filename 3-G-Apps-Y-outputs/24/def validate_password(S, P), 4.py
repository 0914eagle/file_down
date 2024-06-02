
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

# Input
S = input().strip()
P = input().strip()

# Output
print(validate_password(S, P))
