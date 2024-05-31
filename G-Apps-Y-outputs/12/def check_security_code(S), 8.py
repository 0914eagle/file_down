
def check_security_code(S):
    for i in range(len(S) - 1):
        if S[i] == S[i+1]:
            return "Bad"
    return "Good"

S = input().strip()
print(check_security_code(S))
