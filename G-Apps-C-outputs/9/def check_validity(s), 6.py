
def check_validity(s):
    def is_valid(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                if balance == 0:
                    return False
                balance -= 1
        return balance == 0

    if is_valid(s):
        return "possible"

    n = len(s)
    for i in range(n):
        for j in range(i, n):
            new_s = s[:i] + ''.join(['(' if x == ')' else ')' for x in s[i:j+1]]) + s[j+1:]
            if is_valid(new_s):
                return "possible"
    
    return "impossible"

# Read input from user
bracket_sequence = input().strip()
print(check_validity(bracket_sequence))
