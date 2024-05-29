
def match_parens(lst):
    open_count = 0
    close_count = 0
    for string in lst:
        for char in string:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count == 0:
                    close_count += 1
                else:
                    open_count -= 1
    if open_count == 0 and close_count <= 1:
        return 'Yes'
    else:
        return 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'

