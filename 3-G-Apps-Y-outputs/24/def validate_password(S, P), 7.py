
def validate_password(S, P):
    if S == P:
        return "Yes"
    
    if len(P) == len(S) + 1:
        if P[1:] == S or P[:-1] == S:
            return "Yes"
    
    if len(P) == len(S):
        if P.lower() == S or P.upper() == S:
            return "Yes"
    
    return "No"

# Read input
S = input().strip()
P = input().strip()

# Check and print result
print(validate_password(S, P))
