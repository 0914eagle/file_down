
def check_security_code(s):
    for i in range(3):
        if s[i] == s[i+1]:
            print("Bad")
            return
    print("Good")

# Main program
S = input().strip()
check_security_code(S)
