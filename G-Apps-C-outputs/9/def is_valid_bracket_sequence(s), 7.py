
def is_valid_bracket_sequence(s):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def can_make_valid_sequence(s):
    if is_valid_bracket_sequence(s):
        return "possible"

    n = len(s)
    for i in range(n):
        for j in range(i, n):
            segment = s[:i] + ''.join(['(' if x == ')' else ')' for x in s[i:j+1]]) + s[j+1:]
            if is_valid_bracket_sequence(segment):
                return "possible"
    
    return "impossible"

# Test the function
s1 = "()))"
print(can_make_valid_sequence(s1))  # Output: possible

s2 = ")))("
print(can_make_valid_sequence(s2))  # Output: impossible
