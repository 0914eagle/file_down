
def is_valid_bracket_sequence(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')' and stack:
            stack.pop()
        else:
            stack.append(')')
    
    if len(stack) <= 1:
        return "possible"
    
    # Try inverting a segment
    for i in range(len(s)):
        for j in range(i, len(s)):
            new_seq = s[:i] + ''.join(['(' if x == ')' else ')' for x in s[i:j+1]]) + s[j+1:]
            if is_valid_bracket_sequence(new_seq) == "possible":
                return "possible"
    
    return "impossible"

brackets = input().strip()
result = is_valid_bracket_sequence(brackets)
print(result)
