
def match_parens(lst):
    stack = []
    
    for char in lst[0] + lst[1]:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 'No'
    
    return 'Yes' if len(stack) == 0 else 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
