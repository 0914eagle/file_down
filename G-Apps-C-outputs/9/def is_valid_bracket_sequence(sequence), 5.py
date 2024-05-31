
def is_valid_bracket_sequence(sequence):
    stack = []
    
    for bracket in sequence:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(bracket)
    
    if len(stack) == 0:
        return "possible"
    
    if len(stack) == 2:
        return "possible" if stack[0] == '(' and stack[1] == ')' else "impossible"
    
    return "impossible"

# Input
bracket_sequence = input().strip()

# Check if it is possible to make the bracket sequence valid
result = is_valid_bracket_sequence(bracket_sequence)
print(result)
