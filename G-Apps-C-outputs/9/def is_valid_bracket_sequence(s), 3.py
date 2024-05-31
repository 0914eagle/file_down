
def is_valid_bracket_sequence(s):
    def is_valid(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    if is_valid(s):
        return "possible"
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = list(s)
            for k in range(i, j+1):
                if temp[k] == '(':
                    temp[k] = ')'
                else:
                    temp[k] = '('
            if is_valid(temp):
                return "possible"
    
    return "impossible"

# Read input
brackets = input().strip()

# Check validity
result = is_valid_bracket_sequence(brackets)
print(result)
