
def is_valid_bracket_sequence(s):
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

    for i in range(len(s)):
        for j in range(i, len(s)):
            new_s = s[:i] + s[i:j+1][::-1] + s[j+1:]
            if is_valid(new_s):
                return "possible"

    return "impossible"

# Input
bracket_sequence = input().strip()

# Output
print(is_valid_bracket_sequence(bracket_sequence))
