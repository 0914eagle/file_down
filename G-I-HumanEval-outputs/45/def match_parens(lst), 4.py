
def match_parens(lst):
    count = 0
    for char in ''.join(lst):
        if char == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return 'No'
    if count == 0:
        return 'Yes'
    return 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: Yes
print(match_parens([')', ')']))     # Output: No
```
