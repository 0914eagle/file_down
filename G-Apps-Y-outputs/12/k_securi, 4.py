k_security_code(code):
    for i in range(len(code) - 1):
        if code[i] == code[i+1]:
            return "Bad"
    return "Good"

S = input().strip()
print(check_security_code(S))
[/PYTHON