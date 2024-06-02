
def validate_password(S, P):
    if S == P:
        return "Yes"
    
    if len(P) == len(S) + 1 and P[1:] == S:
        return "Yes"
    
    if len(P) == len(S) + 1 and P[:-1] == S:
        return "Yes"
    
    if len(P) == len(S) and P.swapcase() == S:
        return "Yes"
    
    return "No"

# Input
S = input().strip()
P = input().strip()

# Output
print(validate_password(S, P))
