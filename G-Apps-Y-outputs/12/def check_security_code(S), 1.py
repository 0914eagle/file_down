
def check_security_code(S):
    for i in range(3):
        if S[i] == S[i+1]:
            print("Bad")
            return
    print("Good")

S = input()
check_security_code(S)
