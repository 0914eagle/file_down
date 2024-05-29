
def match_parens(lst):
    count = 0

    for char in lst[0] + lst[1]:
        if char == '(':
            count += 1
        elif char == ')':
            if count == 0:
                return 'No'
            count -= 1
    
    return 'Yes' if count == 0 else 'No'

# Test cases
print(match_parens(['()(', ')']))  # Yes
print(match_parens([')', ')']))     # No
