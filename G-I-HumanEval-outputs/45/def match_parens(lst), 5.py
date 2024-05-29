
def match_parens(lst):
    s = lst[0] + lst[1]
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'No'
            stack.pop()

    return 'Yes' if not stack else 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
