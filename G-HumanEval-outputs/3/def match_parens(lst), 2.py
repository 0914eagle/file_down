
def match_parens(lst):
    open_count = 0
    close_count = 0
    for s in lst:
        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                elif open_count == 0:
                    close_count += 1
    return 'Yes' if open_count == 0 and close_count == 0 else 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
```
