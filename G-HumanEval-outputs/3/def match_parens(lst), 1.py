
def match_parens(lst):
    def is_balanced(s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
    
    s1, s2 = lst[0], lst[1]
    combined = s1 + s2
    return 'Yes' if is_balanced(combined) else 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
```
