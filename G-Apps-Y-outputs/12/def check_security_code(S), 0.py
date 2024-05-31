
def check_security_code(S):
    for i in range(3):
        if S[i] == S[i+1]:
            print("Bad")
            return
    print("Good")

# Input
S = input()

# Check security code
check_security_code(S)
[/PYTHON