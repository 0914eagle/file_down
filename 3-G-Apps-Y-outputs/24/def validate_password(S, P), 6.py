
def validate_password(S, P):
    if S == P:
        return "Yes"
    
    if len(S) == len(P) + 1 and S[1:] == P:
        return "Yes"
    
    if len(S) == len(P) + 1 and S[:-1] == P:
        return "Yes"
    
    if S == P.swapcase():
        return "Yes"
    
    return "No"

# Read input
S = input().strip()
P = input().strip()

# Call the function and print the result
print(validate_password(S, P))
