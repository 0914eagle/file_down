
def match_parens(lst):
    combined_str = "".join(lst)
    stack = []
    for s in combined_str:
        if s == '(':
            stack.append('(')
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'No'
    return 'Yes' if not stack else 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
```
