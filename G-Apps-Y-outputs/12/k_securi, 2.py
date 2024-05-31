k_security_code(S):
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            print("Bad")
            return
    print("Good")

# Input
S = input().strip()

# Check security code
check_security_code(S)
[/PYTHON