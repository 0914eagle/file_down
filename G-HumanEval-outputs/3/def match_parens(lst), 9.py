
def match_parens(lst):
    # Concatenate the two strings
    concatenated = lst[0] + lst[1]
    
    # Check if the parentheses are balanced
    stack = []
    for char in concatenated:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'No'
            else:
                stack.pop()
    
    return 'Yes' if not stack else 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
```
