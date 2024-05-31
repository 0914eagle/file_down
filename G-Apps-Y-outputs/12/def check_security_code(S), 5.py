
def check_security_code(S):
    for i in range(3):
        if S[i] == S[i+1]:
            return "Bad"
    return "Good"

# Input
S = input().strip()

# Check security code
result = check_security_code(S)
print(result)
