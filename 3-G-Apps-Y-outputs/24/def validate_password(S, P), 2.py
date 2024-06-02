
def validate_password(S, P):
    if S == P:
        return "Yes"
    if len(P) == len(S) + 1 and P[1:] == S:
        return "Yes"
    if len(P) == len(S) + 1 and P[:-1] == S:
        return "Yes"
    if P.swapcase() == S:
        return "Yes"
    return "No"

# Read input
S = input().strip()
P = input().strip()

# Call the function and print the result
print(validate_password(S, P))
