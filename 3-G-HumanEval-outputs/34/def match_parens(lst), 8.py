
def match_parens(lst):
    stack = []
    for s in lst:
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return 'No'
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: Yes
print(match_parens([')', ')']))     # Output: No
